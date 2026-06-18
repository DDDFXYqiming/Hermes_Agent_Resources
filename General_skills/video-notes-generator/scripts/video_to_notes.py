#!/usr/bin/env python3
"""
Video Notes Generator — 核心脚本 (零pip依赖版本)
依赖: yt-dlp (二进制), ffmpeg (系统包)
无需安装任何 Python 扩展包。whisper.cpp 可选，有则自动转写。

用法:
    python3 video_to_notes.py <video_url> [--output ./notes]
    python3 video_to_notes.py <video_url> --transcribe --model base
    # Frames, visual manifest, Markdown image embeds, and opening Mermaid mind map are enabled by default.
"""

import argparse
import json
import os
import platform as _platform_module
import re
import shutil
import subprocess
import sys
import tempfile
import ssl
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass, field
from datetime import timedelta
from pathlib import Path
from typing import List, Optional


def _cleanup_agent_browser_chrome():
    """Kill leftover agent-browser-chrome temporary profile processes.

    These are NOT created by this script; they come from the Agent's browser_*
    tools (e.g. browser_navigate / browser_snapshot) when the underlying Chrome
    automation crashes or exits uncleanly. On Windows they accumulate under
    --user-data-dir=...\agent-browser-chrome-<uuid> and can consume several GB
    of RAM over time. We clean them at script startup to avoid resource leaks.
    """
    if _platform_module.system() != "Windows":
        try:
            subprocess.run(
                ["pkill", "-f", "agent-browser-chrome"],
                capture_output=True, timeout=15
            )
        except Exception:
            pass
        return
    # Windows: find chrome.exe roots with agent-browser-chrome in cmdline but no --type=
    try:
        result = subprocess.run(
            ["wmic", "process", "where", "name='chrome.exe'", "get", "ProcessId,CommandLine", "/format:csv"],
            capture_output=True, text=True, timeout=30, encoding="utf-8", errors="replace"
        )
        if result.returncode != 0:
            return
        roots = []
        for line in result.stdout.splitlines():
            if "agent-browser-chrome" not in line:
                continue
            if "--type=" in line:
                continue
            # CSV format: Node,ProcessId,CommandLine
            parts = line.split(",")
            if len(parts) >= 2:
                try:
                    pid = int(parts[1].strip().strip('"'))
                    roots.append(pid)
                except ValueError:
                    continue
        for pid in roots:
            try:
                subprocess.run(
                    ["taskkill", "/F", "/T", "/PID", str(pid)],
                    capture_output=True, timeout=15
                )
            except Exception:
                pass
    except Exception:
        pass


_cleanup_agent_browser_chrome()

# ============================================================
# 数据模型
# ============================================================

@dataclass
class TranscriptSegment:
    start: float
    end: float
    text: str

@dataclass
class TranscriptResult:
    language: Optional[str] = None
    full_text: str = ""
    segments: List[TranscriptSegment] = field(default_factory=list)

@dataclass
class AudioMeta:
    video_id: str = ""
    title: str = ""
    duration: float = 0
    platform: str = ""
    file_path: str = ""
    raw_info: dict = field(default_factory=dict)

@dataclass
class VideoInfo:
    video_url: str = ""
    video_id: str = ""
    title: str = ""
    platform: str = ""
    uploader: str = ""
    duration: float = 0
    view_count: int = 0
    like_count: int = 0
    tags: List[str] = field(default_factory=list)
    description: str = ""
    chapters: List[dict] = field(default_factory=list)

@dataclass
class FrameInfo:
    index: int
    timestamp: float
    timestamp_text: str
    image_path: str
    nearby_transcript: str = ""
    visual_note: str = ""

@dataclass
class TranscribeOutput:
    video_info: dict = field(default_factory=dict)
    transcript_text: str = ""
    segments: List[dict] = field(default_factory=list)
    chapters: List[dict] = field(default_factory=list)
    source: str = ""
    output_file: str = ""
    visual_frames: List[dict] = field(default_factory=list)
    visual_manifest_file: str = ""
    notes_md: str = ""  # 由 Agent 填充的 Markdown 笔记
    chunk_summaries_file: str = ""
    final_notes_file: str = ""

# ============================================================
# 工具函数
# ============================================================

RUNTIME_DIR = os.getenv("VIDEO_NOTES_RUNTIME_DIR") or os.path.join(
    os.path.expanduser("~"),
    ".cache",
    "video-notes-generator",
)


def load_runtime_env():
    env_file = os.getenv("VIDEO_NOTES_ENV", os.path.join(RUNTIME_DIR, ".env"))
    if not os.path.isfile(env_file):
        return
    with open(env_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())


load_runtime_env()

YTDLP = os.getenv("YTDLP") or shutil.which("yt-dlp") or os.path.expanduser("~/.local/bin/yt-dlp")
FFMPEG = os.getenv("FFMPEG") or shutil.which("ffmpeg") or "ffmpeg"
WHISPER_CPP_PATH = os.getenv("WHISPER_CPP", "")
WHISPER_MODEL = os.getenv("WHISPER_MODEL", "base").lower()
TRANSCRIBER_TYPE = os.getenv("TRANSCRIBER_TYPE", "faster-whisper").lower()
TRANSCRIPT_CHUNK_CHARS = int(os.getenv("VIDEO_NOTES_TRANSCRIPT_CHUNK_CHARS", "3200"))
NOTES_TRANSCRIPT_PREVIEW_CHARS = int(os.getenv("VIDEO_NOTES_TRANSCRIPT_PREVIEW_CHARS", "1200"))
MAX_AGENT_FRAMES = int(os.getenv("VIDEO_NOTES_MAX_AGENT_FRAMES", "3"))
FRAME_MAX_WIDTH = int(os.getenv("VIDEO_NOTES_FRAME_MAX_WIDTH", "640"))
VIDEO_NOTES_PROXY = os.getenv("VIDEO_NOTES_PROXY", "").strip()
VIDEO_NOTES_PROXY_CONFIG = os.getenv("VIDEO_NOTES_PROXY_CONFIG", "")
WHISPER_MODEL_CONFIG = os.getenv("VIDEO_NOTES_WHISPER_MODEL_CONFIG", "")

# BiliNote v2.4.0 made proxy and Whisper model handling explicit.
# Keep this script zero-pip, but mirror the same operator-facing behavior.
BUILTIN_FASTER_WHISPER_MODELS = {
    "tiny": "Systran/faster-whisper-tiny",
    "base": "Systran/faster-whisper-base",
    "small": "Systran/faster-whisper-small",
    "medium": "Systran/faster-whisper-medium",
    "large-v1": "Systran/faster-whisper-large-v1",
    "large-v2": "Systran/faster-whisper-large-v2",
    "large-v3": "Systran/faster-whisper-large-v3",
    "large-v3-turbo": "Systran/faster-whisper-large-v3-turbo",
}


def runtime_path(*parts):
    return os.path.join(RUNTIME_DIR, *parts)


def _read_json_file(path: str) -> dict:
    if not path or not os.path.isfile(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f) or {}
        return data if isinstance(data, dict) else {}
    except Exception as e:
        print(f"[config] 读取 JSON 配置失败 {path}: {e}", file=sys.stderr)
        return {}


def get_effective_proxy() -> str:
    """Return the proxy URL that should apply to yt-dlp and network helpers.

    Mirrors BiliNote v2.4.0's precedence in a zero-pip CLI form:
    explicit VIDEO_NOTES_PROXY > enabled runtime config/proxy.json > standard
    HTTPS_PROXY/HTTP_PROXY/ALL_PROXY environment variables.
    """
    explicit_proxy = os.getenv("VIDEO_NOTES_PROXY", VIDEO_NOTES_PROXY).strip()
    if explicit_proxy:
        return explicit_proxy
    proxy_config = os.getenv("VIDEO_NOTES_PROXY_CONFIG", VIDEO_NOTES_PROXY_CONFIG) or runtime_path("config", "proxy.json")
    cfg = _read_json_file(proxy_config)
    if cfg.get("enabled") and str(cfg.get("url") or "").strip():
        return str(cfg.get("url")).strip()
    for key in ("HTTPS_PROXY", "https_proxy", "HTTP_PROXY", "http_proxy", "ALL_PROXY", "all_proxy"):
        val = os.environ.get(key)
        if val:
            return val
    return ""


def yt_dlp_args() -> List[str]:
    args = [YTDLP]
    proxy = get_effective_proxy()
    if proxy:
        args.extend(["--proxy", proxy])
    return args


def bilibili_headers(referer: str = "https://www.bilibili.com/") -> dict:
    return {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
        "Referer": referer,
        "Accept": "*/*",
    }


def extract_bilibili_bvid(url: str) -> str:
    m = re.search(r"BV[0-9A-Za-z]+", url or "")
    return m.group(0) if m else ""


def fetch_json_url(url: str, headers: Optional[dict] = None, timeout: int = 30) -> Optional[dict]:
    try:
        req = urllib.request.Request(url, headers=headers or {})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            text = resp.read().decode("utf-8", errors="replace")
        data = json.loads(text)
        return data if isinstance(data, dict) else None
    except Exception as e:
        print(f"[network] JSON 获取失败: {url.split('?')[0]}: {e}", file=sys.stderr)
        return None


def get_bilibili_api_metadata(url: str) -> Optional[dict]:
    bvid = extract_bilibili_bvid(url)
    if not bvid:
        return None
    referer = f"https://www.bilibili.com/video/{bvid}/"
    data = fetch_json_url(
        f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}",
        headers=bilibili_headers(referer),
    )
    if not data or data.get("code") != 0 or not isinstance(data.get("data"), dict):
        return None
    return data["data"]


def bilibili_metadata_to_video_info(url: str, data: dict) -> VideoInfo:
    owner = data.get("owner") or {}
    stat = data.get("stat") or {}
    return VideoInfo(
        video_url=url,
        video_id=data.get("bvid", extract_bilibili_bvid(url)),
        title=data.get("title", ""),
        platform="bilibili",
        uploader=owner.get("name", ""),
        duration=parse_duration(data.get("duration", 0)),
        view_count=int(stat.get("view", 0) or 0),
        like_count=int(stat.get("like", 0) or 0),
        tags=[],
        description=(data.get("desc", "") or "")[:500],
        chapters=[],
    )


def get_bilibili_api_playurl(url: str, cid: int) -> Optional[dict]:
    bvid = extract_bilibili_bvid(url)
    if not bvid or not cid:
        return None
    referer = f"https://www.bilibili.com/video/{bvid}/"
    api = f"https://api.bilibili.com/x/player/playurl?bvid={bvid}&cid={cid}&qn=32&fnval=16&fourk=0"
    data = fetch_json_url(api, headers=bilibili_headers(referer))
    if not data or data.get("code") != 0:
        return None
    return data.get("data") or {}


def bilibili_dash_url_candidates(items: list, prefer_audio: bool = False) -> List[str]:
    if not items:
        return []
    # Some Bilibili CDN hosts occasionally return short/partial audio objects.
    # Try normal bilivideo hosts before mcdn, and verify duration after download.
    def score(item):
        bw = int(item.get("bandwidth", 0) or 0)
        url = item.get("baseUrl") or item.get("base_url") or ""
        mcdn_penalty = 1 if "mcdn.bilivideo" in url else 0
        return (mcdn_penalty, -bw if prefer_audio else bw)
    urls = []
    for item in sorted(items, key=score):
        for key in ("baseUrl", "base_url"):
            if item.get(key):
                urls.append(item[key])
        for key in ("backupUrl", "backup_url"):
            for url in item.get(key) or []:
                urls.append(url)
    seen = set()
    unique = []
    for url in urls:
        if url and url not in seen:
            seen.add(url)
            unique.append(url)
    return unique


def download_url_to_file(url: str, dest: str, referer: str) -> bool:
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    headers = bilibili_headers(referer)
    curl = shutil.which("curl")
    if curl:
        cmd = [
            curl, "-L", "-k", "--fail", "--retry", "3", "--retry-delay", "2",
            "-A", headers["User-Agent"], "-e", headers["Referer"], url, "-o", dest,
        ]
        result = run_command(cmd, timeout=600, env=command_env())
        if result.returncode == 0 and os.path.getsize(dest) > 0:
            return True
        print(f"[bilibili-api] curl 下载失败: {result.stderr[:200]}", file=sys.stderr)
    try:
        context = ssl._create_unverified_context()
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=600, context=context) as resp, open(dest, "wb") as f:
            shutil.copyfileobj(resp, f)
        return os.path.getsize(dest) > 0
    except Exception as e:
        print(f"[bilibili-api] urllib 下载失败: {e}", file=sys.stderr)
        return False



def download_bilibili_stream_candidates(urls: List[str], dest: str, referer: str, expected_duration: float, selector: str) -> bool:
    min_duration = max(30.0, float(expected_duration or 0) * 0.80) if expected_duration else 0.0
    for idx, stream_url in enumerate(urls, start=1):
        # curl -o / Python open(..., 'wb') overwrites the candidate file in place;
        # avoid explicit deletion so partial retry remains harmless and auditable.
        print(f"[bilibili-api] 下载候选流 {idx}/{len(urls)} -> {os.path.basename(dest)}", file=sys.stderr)
        if not download_url_to_file(stream_url, dest, referer):
            continue
        duration = probe_stream_duration(dest, selector) or probe_media_duration(dest)
        if not min_duration or duration >= min_duration:
            return True
        print(
            f"[bilibili-api] 候选流时长异常: {duration:.1f}s，期望约 {expected_duration:.1f}s，尝试下一个 CDN",
            file=sys.stderr,
        )
    return False



def merged_file_has_valid_streams(path: str, expected_duration: float) -> bool:
    if not os.path.exists(path):
        return False
    min_duration = max(30.0, float(expected_duration or 0) * 0.80) if expected_duration else 0.0
    video_duration = probe_stream_duration(path, "v:0")
    audio_duration = probe_stream_duration(path, "a:0")
    if not min_duration:
        return video_duration > 0 and audio_duration > 0
    return video_duration >= min_duration and audio_duration >= min_duration


def download_bilibili_via_api(url: str, output_dir: str) -> Optional[AudioMeta]:
    """Fallback for public Bilibili videos when yt-dlp hits HTTP 412.

    Uses public metadata/playurl APIs, downloads DASH video/audio with browser-like
    headers, muxes them to a local mp4, and returns that mp4 for transcription and
    frame extraction. No cookies or API keys are written.
    """
    metadata = get_bilibili_api_metadata(url)
    if not metadata:
        return None
    bvid = metadata.get("bvid") or extract_bilibili_bvid(url) or "bilibili"
    safe_bvid = re.sub(r"[^\w-]", "", bvid)[:50]
    fallback_dir = os.path.join(output_dir, f"{safe_bvid}_bilibili_api")
    os.makedirs(fallback_dir, exist_ok=True)
    merged = os.path.join(fallback_dir, f"{safe_bvid}_merged.mp4")
    expected_duration = parse_duration(metadata.get("duration", 0))
    if merged_file_has_valid_streams(merged, expected_duration):
        return AudioMeta(
            video_id=bvid,
            title=metadata.get("title", bvid),
            duration=probe_media_duration(merged),
            platform="bilibili",
            file_path=merged,
            raw_info={"fallback": "bilibili_api", "metadata": metadata},
        )
    play = get_bilibili_api_playurl(url, metadata.get("cid"))
    dash = (play or {}).get("dash") or {}
    video_urls = bilibili_dash_url_candidates(dash.get("video") or [], prefer_audio=False)
    audio_urls = bilibili_dash_url_candidates(dash.get("audio") or [], prefer_audio=True)
    if not video_urls or not audio_urls:
        print("[bilibili-api] playurl 未返回可用 DASH 音视频流", file=sys.stderr)
        return None
    referer = f"https://www.bilibili.com/video/{bvid}/"
    video_file = os.path.join(fallback_dir, f"{safe_bvid}_video.m4s")
    audio_file = os.path.join(fallback_dir, f"{safe_bvid}_audio.m4s")
    metadata_file = os.path.join(fallback_dir, f"{safe_bvid}_metadata.json")
    with open(metadata_file, "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    print("[bilibili-api] yt-dlp 不可用，使用 Bilibili API fallback 下载 DASH 音视频...", file=sys.stderr)
    if not download_bilibili_stream_candidates(video_urls, video_file, referer, expected_duration, "v:0"):
        return None
    if not download_bilibili_stream_candidates(audio_urls, audio_file, referer, expected_duration, "a:0"):
        return None
    result = run_command([FFMPEG, "-y", "-i", video_file, "-i", audio_file, "-c", "copy", merged], timeout=300, env=command_env())
    if result.returncode != 0 or not os.path.exists(merged):
        print(f"[bilibili-api] ffmpeg 合并失败: {result.stderr[:300]}", file=sys.stderr)
        return None
    return AudioMeta(
        video_id=bvid,
        title=metadata.get("title", bvid),
        duration=probe_media_duration(merged) or expected_duration,
        platform="bilibili",
        file_path=merged,
        raw_info={"fallback": "bilibili_api", "metadata": metadata, "metadata_file": metadata_file},
    )


def resolve_faster_whisper_model(model: str) -> str:
    """Resolve built-in/custom Faster Whisper model names.

    Custom mappings live in VIDEO_NOTES_WHISPER_MODEL_CONFIG or
    <runtime>/config/whisper_models.json as {"name": "HF/repo-or-local-path"}.
    This mirrors BiliNote v2.4.0's configurable model registry without
    introducing a server-side dependency tree.
    """
    name = (model or "base").strip()
    custom_path = os.getenv("VIDEO_NOTES_WHISPER_MODEL_CONFIG", WHISPER_MODEL_CONFIG) or runtime_path("config", "whisper_models.json")
    custom = _read_json_file(custom_path)
    target = custom.get(name)
    if isinstance(target, dict):
        target = target.get("target")
    if isinstance(target, str) and target.strip():
        return target.strip()
    if name in BUILTIN_FASTER_WHISPER_MODELS:
        # Faster Whisper accepts size aliases directly and using aliases preserves
        # offline cache compatibility; the explicit map documents valid options.
        return name
    if "/" in name or os.path.isdir(os.path.expanduser(name)):
        return os.path.expanduser(name)
    raise ValueError(
        f"未知 faster-whisper 模型 '{name}'。内置可选: {', '.join(BUILTIN_FASTER_WHISPER_MODELS)}；"
        "或在 VIDEO_NOTES_WHISPER_MODEL_CONFIG / config/whisper_models.json 中添加映射。"
    )


def run_command(cmd, timeout=60, env=None, cwd=None, check=False):
    command_env_vars = dict(os.environ)
    if env:
        command_env_vars.update(env)
    command_env_vars.setdefault("PYTHONIOENCODING", "utf-8")
    command_env_vars.setdefault("PYTHONUTF8", "1")
    return subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=timeout,
        env=command_env_vars,
        cwd=cwd,
        check=check,
        encoding="utf-8",
        errors="replace",
    )


def command_env():
    path_entries = [
        os.path.expanduser("~/.local/bin"),
        runtime_path("bin"),
        os.path.dirname(FFMPEG) if os.path.isabs(FFMPEG) else "",
        os.environ.get("PATH", ""),
    ]
    env = {"PATH": os.pathsep.join(p for p in path_entries if p)}
    proxy = get_effective_proxy()
    if proxy:
        env.setdefault("HTTP_PROXY", proxy)
        env.setdefault("HTTPS_PROXY", proxy)
    return env


def get_ffprobe() -> str:
    if os.getenv("FFPROBE"):
        return os.getenv("FFPROBE")
    if os.path.isabs(FFMPEG):
        candidate = os.path.join(os.path.dirname(FFMPEG), "ffprobe.exe" if os.name == "nt" else "ffprobe")
        if os.path.isfile(candidate):
            return candidate
    return shutil.which("ffprobe") or "ffprobe"


def probe_media_duration(path: str) -> float:
    if not path or not os.path.exists(path):
        return 0.0
    try:
        result = run_command([
            get_ffprobe(), "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", path
        ], timeout=30, env=command_env())
        if result.returncode == 0:
            return parse_duration((result.stdout or "").strip())
    except Exception:
        pass
    return 0.0


def probe_stream_duration(path: str, selector: str) -> float:
    if not path or not os.path.exists(path):
        return 0.0
    try:
        result = run_command([
            get_ffprobe(), "-v", "error", "-select_streams", selector,
            "-show_entries", "stream=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", path
        ], timeout=30, env=command_env())
        if result.returncode == 0:
            durations = [parse_duration(line.strip()) for line in (result.stdout or "").splitlines() if line.strip()]
            durations = [d for d in durations if d > 0]
            return max(durations) if durations else 0.0
    except Exception:
        pass
    return 0.0

def check_deps():
    """检查必要工具"""
    issues = []
    if not os.path.exists(YTDLP):
        issues.append(
            f"yt-dlp 未安装: mkdir -p ~/.local/bin && "
            f"curl -fsSL -o ~/.local/bin/yt-dlp "
            f"https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp "
            f"&& chmod +x ~/.local/bin/yt-dlp"
        )
    if not (shutil.which(FFMPEG) or os.path.isfile(FFMPEG)):
        issues.append(
            f"ffmpeg 未安装: apt install ffmpeg (或 brew install ffmpeg)"
        )
    return issues

def get_whisper_cpp():
    """查找 whisper.cpp 二进制"""
    if WHISPER_CPP_PATH and os.path.isfile(WHISPER_CPP_PATH):
        return WHISPER_CPP_PATH

    candidates = [
        "whisper-cli",
        "whisper.cpp",
        os.path.expanduser("~/whisper.cpp/build/bin/whisper-cli"),
        os.path.expanduser("~/whisper.cpp/main"),
        "/tmp/whisper.cpp/build/bin/whisper-cli",
    ]
    for p in candidates:
        if shutil.which(p) or os.path.isfile(p):
            return os.path.abspath(p) if os.path.isfile(p) else shutil.which(p)
    return None

def auto_compile_whisper_cpp():
    """自动下载并编译 whisper.cpp"""
    target_dir = os.path.expanduser("~/whisper.cpp")
    cmake_bin_dir = "/tmp/cmake-bin/bin"

    if os.path.isfile(os.path.join(target_dir, "build", "bin", "whisper-cli")):
        return os.path.join(target_dir, "build", "bin", "whisper-cli")

    print("[transcribe] whisper.cpp 未找到，尝试自动编译...", file=sys.stderr)

    # 检查编译工具
    for tool in ["gcc", "g++", "make"]:
        if not shutil.which(tool):
            print(f"[transcribe] 缺少编译工具: {tool}", file=sys.stderr)
            return None

    # 下载 cmake
    cmake_bin = os.path.join(cmake_bin_dir, "cmake")
    if not os.path.isfile(cmake_bin):
        print("[transcribe] 下载 cmake...", file=sys.stderr)
        os.makedirs(cmake_bin_dir, exist_ok=True)
        try:
            subprocess.run(
                ["curl", "-fsSL", "-o", "/tmp/cmake.tar.gz",
                 "https://github.com/Kitware/CMake/releases/download/v3.28.1/cmake-3.28.1-linux-x86_64.tar.gz"],
                capture_output=True, timeout=120, check=True
            )
            subprocess.run(
                ["tar", "xzf", "/tmp/cmake.tar.gz", "--strip-components=1", "-C", cmake_bin_dir],
                capture_output=True, timeout=60, check=True
            )
            print(f"[transcribe] cmake 安装完成", file=sys.stderr)
        except Exception as e:
            print(f"[transcribe] cmake 安装失败: {e}", file=sys.stderr)
            return None

    # 克隆 whisper.cpp
    if os.path.exists(target_dir):
        print("[transcribe] 更新 whisper.cpp...", file=sys.stderr)
        subprocess.run(["git", "pull", "--depth", "1"], cwd=target_dir, capture_output=True)
    else:
        print("[transcribe] 克隆 whisper.cpp...", file=sys.stderr)
        subprocess.run(
            ["git", "clone", "--depth", "1", "https://github.com/ggerganov/whisper.cpp.git", target_dir],
            capture_output=True, timeout=120
        )

    # 编译
    print("[transcribe] 编译 whisper.cpp (可能需要几分钟)...", file=sys.stderr)
    try:
        subprocess.run(
            [cmake_bin, "-S", target_dir, "-B", os.path.join(target_dir, "build"),
             "-DWHISPER_CUDA=OFF"],
            capture_output=True, timeout=120, check=True
        )
        subprocess.run(
            [cmake_bin, "--build", os.path.join(target_dir, "build"),
             "--config", "Release", "-j", str(os.cpu_count() or 4)],
            capture_output=True, timeout=600, check=True
        )
        print("[transcribe] whisper.cpp 编译完成!", file=sys.stderr)
    except subprocess.TimeoutExpired:
        print("[transcribe] 编译超时", file=sys.stderr)
        return None
    except Exception as e:
        print(f"[transcribe] 编译失败: {e}", file=sys.stderr)
        return None

    return os.path.join(target_dir, "build", "bin", "whisper-cli")

def transcribe_via_whisper_cpp(audio_path: str, model: str = "base") -> Optional[List[TranscriptSegment]]:
    """使用 whisper.cpp 转写音频"""
    # 检查 whisper.cpp
    whisper_bin = get_whisper_cpp()
    if not whisper_bin:
        whisper_bin = auto_compile_whisper_cpp()
    if not whisper_bin:
        print("[transcribe] 无法获取 whisper.cpp，跳过转写", file=sys.stderr)
        return None

    # 推断 whisper.cpp 根目录（向上回溯）
    whisper_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(whisper_bin))))
    model_dirs = [
        os.path.expanduser("~/.local/share/whisper.cpp/models"),
        os.path.join(whisper_root, "models"),
        os.path.join(os.path.dirname(whisper_bin), "models"),
    ]

    # 查找模型文件
    model_file = None
    for model_dir in model_dirs:
        for ext in [".gguf", ".ggml", ".bin", ".q5_1.bin", ".q8_0.bin"]:
            candidate = os.path.join(model_dir, f"ggml-{model}{ext}")
            if os.path.exists(candidate):
                model_file = candidate
                break
        if model_file:
            break

    if not model_file:
        print(f"[transcribe] 模型 {model} 未找到，尝试自动下载...", file=sys.stderr)
        try:
            download_script = os.path.join(whisper_root, "models", "download-ggml-model.sh")
            if os.path.exists(download_script):
                subprocess.run(
                    ["bash", download_script, model],
                    capture_output=True, timeout=300, cwd=whisper_root
                )
            for mdir in model_dirs:
                for ext in [".gguf", ".ggml", ".bin", ".q5_1.bin", ".q8_0.bin"]:
                    candidate = os.path.join(mdir, f"ggml-{model}{ext}")
                    if os.path.exists(candidate):
                        model_file = candidate
                        break
                if model_file:
                    break
        except Exception as e:
            print(f"[transcribe] 模型下载失败: {e}", file=sys.stderr)

    if not model_file:
        print(f"[transcribe] whisper.cpp: 模型获取失败，跳过转写", file=sys.stderr)
        return None

    # whisper.cpp 只能读 WAV，先转换
    wav_path = audio_path
    if not audio_path.lower().endswith(".wav"):
        wav_path = audio_path + ".converted.wav"
        print("[transcribe] 转换音频为 WAV 格式...", file=sys.stderr)
        subprocess.run(
            [FFMPEG, "-y", "-i", audio_path, "-ar", "16000", "-ac", "1", "-f", "wav", wav_path],
            capture_output=True, timeout=300
        )

    print(f"[transcribe] whisper.cpp 转写中 (model={model})...", file=sys.stderr)
    try:
        result = subprocess.run(
            [whisper_bin, "-m", model_file, "-f", wav_path,
             "-l", "zh", "--print-colors", "0"],
            capture_output=True, text=True, timeout=3600, encoding="utf-8", errors="replace"
        )

        segments = []
        for line in result.stdout.split("\n"):
            match = re.match(r"\[(\d{2}:\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}:\d{2}\.\d{3})\]\s*(.+)", line)
            if match:
                def parse_whisper_time(ts: str) -> float:
                    parts = ts.split(":")
                    return float(parts[0]) * 3600 + float(parts[1]) * 60 + float(parts[2])
                start = parse_whisper_time(match.group(1))
                end = parse_whisper_time(match.group(2))
                text = match.group(3).strip()
                if text:
                    segments.append(TranscriptSegment(start=start, end=end, text=text))

        # 清理临时 wav 文件
        if wav_path != audio_path and os.path.exists(wav_path):
            os.remove(wav_path)

        if segments:
            print(f"[transcribe] 转写完成: {len(segments)} 段", file=sys.stderr)
        return segments if segments else None

    except Exception as e:
        print(f"[transcribe] whisper.cpp 转写失败: {e}", file=sys.stderr)
        return None


def transcribe_via_faster_whisper(audio_path: str, model: str = "base") -> Optional[List[TranscriptSegment]]:
    try:
        os.environ.setdefault("HF_HOME", runtime_path("hf-cache"))
        os.environ.setdefault("HUGGINGFACE_HUB_CACHE", runtime_path("hf-cache", "hub"))
        os.environ.setdefault("XDG_CACHE_HOME", runtime_path("cache"))
        from faster_whisper import WhisperModel
    except Exception as e:
        print(f"[transcribe] faster-whisper 不可用: {e}", file=sys.stderr)
        return None

    try:
        os.makedirs(runtime_path("models"), exist_ok=True)
        resolved_model = resolve_faster_whisper_model(model)
        print(f"[transcribe] faster-whisper 转写中 (model={model} -> {resolved_model})...", file=sys.stderr)
        whisper_model = WhisperModel(
            resolved_model,
            device=os.getenv("WHISPER_DEVICE", "cpu"),
            compute_type=os.getenv("WHISPER_COMPUTE_TYPE", "int8"),
            download_root=runtime_path("models"),
        )
        raw_segments, _ = whisper_model.transcribe(audio_path, language="zh", vad_filter=True)
        segments = [TranscriptSegment(start=s.start, end=s.end, text=s.text.strip()) for s in raw_segments if s.text.strip()]
        if segments:
            print(f"[transcribe] faster-whisper 转写完成: {len(segments)} 段", file=sys.stderr)
        return segments if segments else None
    except Exception as e:
        print(f"[transcribe] faster-whisper 转写失败: {e}", file=sys.stderr)
        return None

# ============================================================
# SRT 字幕解析器 (纯标准库)
# ============================================================

def parse_srt(srt_text: str) -> List[TranscriptSegment]:
    """解析 SRT 字幕"""
    segments = []
    blocks = re.split(r"\n\n+", srt_text.strip())
    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) < 3:
            continue
        time_match = re.match(r"(\d{2}:\d{2}:\d{2}[,.]\d+)\s*-->\s*(\d{2}:\d{2}:\d{2}[,.]\d+)", lines[1])
        if not time_match:
            continue
        def parse_time(ts: str) -> float:
            ts = ts.replace(",", ".")
            parts = ts.split(":")
            return float(parts[0]) * 3600 + float(parts[1]) * 60 + float(parts[2])
        start = parse_time(time_match.group(1))
        end = parse_time(time_match.group(2))
        text = "\n".join(lines[2:]).strip()
        if text:
            segments.append(TranscriptSegment(start=start, end=end, text=text))
    return segments

def parse_vtt(vtt_text: str) -> List[TranscriptSegment]:
    """Parse WebVTT subtitles emitted by yt-dlp/YouTube fallback."""
    text = vtt_text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"<[^>]+>", "", text)
    segments = []
    blocks = re.split(r"\n\n+", text.strip())
    for block in blocks:
        lines = [line.strip() for line in block.split("\n") if line.strip()]
        if not lines or lines[0].upper().startswith("WEBVTT") or lines[0].startswith(("NOTE", "STYLE", "REGION")):
            continue
        time_line_index = next((i for i, line in enumerate(lines) if "-->" in line), -1)
        if time_line_index < 0:
            continue
        time_line = lines[time_line_index]
        time_match = re.match(r"([^\s]+)\s*-->\s*([^\s]+)", time_line)
        if not time_match:
            continue
        def parse_vtt_time(ts: str) -> float:
            ts = ts.replace(",", ".")
            parts = ts.split(":")
            parts = [float(p) for p in parts]
            if len(parts) == 3:
                return parts[0] * 3600 + parts[1] * 60 + parts[2]
            if len(parts) == 2:
                return parts[0] * 60 + parts[1]
            return parts[0]
        body = " ".join(lines[time_line_index + 1:]).strip()
        body = re.sub(r"\s+", " ", body)
        if body:
            segments.append(TranscriptSegment(
                start=parse_vtt_time(time_match.group(1)),
                end=parse_vtt_time(time_match.group(2)),
                text=body,
            ))
    return segments


def parse_duration(seconds) -> float:
    try:
        return float(seconds)
    except (TypeError, ValueError):
        pass
    if isinstance(seconds, str):
        parts = seconds.split(":")
        parts = [float(p) for p in parts]
        if len(parts) == 3:
            return parts[0] * 3600 + parts[1] * 60 + parts[2]
        elif len(parts) == 2:
            return parts[0] * 60 + parts[1]
    return 0.0


def format_timestamp(seconds: float) -> str:
    seconds = max(0, float(seconds or 0))
    total = int(seconds)
    return f"{total // 60:02d}:{total % 60:02d}"


def find_nearby_transcript(segments: List[dict], timestamp: float, window: float = 8.0) -> str:
    nearby = []
    for segment in segments:
        start = float(segment.get("start", 0) or 0)
        end = float(segment.get("end", start) or start)
        if start - window <= timestamp <= end + window:
            text = str(segment.get("text", "")).strip()
            if text:
                nearby.append(text)
    return " ".join(nearby)[:500]


def compact_text(text: str, limit: int) -> str:
    text = " ".join(str(text or "").split())
    if len(text) <= limit:
        return text
    return text[: max(0, limit - 1)].rstrip() + "..."


def chunk_transcript_segments(segments: List[dict], max_chars: int = TRANSCRIPT_CHUNK_CHARS) -> List[dict]:
    chunks = []
    current = []
    current_len = 0
    max_chars = max(800, int(max_chars or TRANSCRIPT_CHUNK_CHARS))

    for segment in segments:
        text = " ".join(str(segment.get("text", "")).split())
        if not text:
            continue
        projected = current_len + len(text) + 1
        if current and projected > max_chars:
            chunks.append({"segments": current})
            current = []
            current_len = 0
        current.append(segment)
        current_len += len(text) + 1

    if current:
        chunks.append({"segments": current})

    for index, chunk in enumerate(chunks, start=1):
        chunk_segments = chunk["segments"]
        text = " ".join(str(s.get("text", "")).strip() for s in chunk_segments if str(s.get("text", "")).strip())
        chunk["index"] = index
        chunk["start"] = float(chunk_segments[0].get("start", 0) or 0)
        chunk["end"] = float(chunk_segments[-1].get("end", chunk["start"]) or chunk["start"])
        chunk["text"] = text
        chunk["char_count"] = len(text)
    return chunks


def build_chunk_summaries_markdown(output: TranscribeOutput, safe_id: str) -> str:
    info = output.video_info or {}
    title = info.get("title") or safe_id
    chunks = chunk_transcript_segments(output.segments)

    lines = [
        f"# {title} - chunk summaries",
        "",
        "This file is intentionally compact. Use it before reading full transcript JSON.",
        "",
        f"- Source: {output.source or 'unknown'}",
        f"- SegmentCount: {len(output.segments)}",
        f"- ChunkCount: {len(chunks)}",
        f"- ChunkCharBudget: {TRANSCRIPT_CHUNK_CHARS}",
        "",
    ]

    if not chunks:
        lines.append("No transcript chunks available.")
        return "\n".join(lines).rstrip() + "\n"

    for chunk in chunks:
        lines.extend([
            f"## Chunk {chunk['index']} [{format_timestamp(chunk['start'])}-{format_timestamp(chunk['end'])}]",
            "",
            f"- Segments: {len(chunk['segments'])}",
            f"- Characters: {chunk['char_count']}",
            f"- Digest: {compact_text(chunk['text'], 900)}",
            "",
        ])
    return "\n".join(lines).rstrip() + "\n"

# ============================================================
# 视频信息 + 字幕获取
# ============================================================

def get_video_info(url: str, platform: str) -> VideoInfo:
    print(f"[info] 获取视频元数据...", file=sys.stderr)
    if platform == "local" and os.path.isfile(url):
        return VideoInfo(
            video_url=os.path.abspath(url),
            video_id=os.path.basename(url),
            title=os.path.splitext(os.path.basename(url))[0],
            platform=platform,
            duration=probe_media_duration(url),
        )
    cmd = yt_dlp_args() + ["--dump-json", "--no-playlist", "--skip-download"]
    result = run_command(cmd + [url], timeout=60, env=command_env())

    if result.returncode != 0:
        if platform == "bilibili":
            metadata = get_bilibili_api_metadata(url)
            if metadata:
                print("[info] yt-dlp 元数据失败，已使用 Bilibili API 元数据 fallback", file=sys.stderr)
                return bilibili_metadata_to_video_info(url, metadata)
        return VideoInfo(video_url=url, video_id=url.split("/")[-1][:50], platform=platform)
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        if platform == "bilibili":
            metadata = get_bilibili_api_metadata(url)
            if metadata:
                print("[info] yt-dlp 元数据 JSON 解析失败，已使用 Bilibili API 元数据 fallback", file=sys.stderr)
                return bilibili_metadata_to_video_info(url, metadata)
        return VideoInfo(video_url=url, platform=platform)

    return VideoInfo(
        video_url=url,
        video_id=data.get("id", ""),
        title=data.get("title", ""),
        platform=platform,
        uploader=data.get("uploader", ""),
        duration=parse_duration(data.get("duration", 0)),
        view_count=data.get("view_count", 0) or 0,
        like_count=data.get("like_count", 0) or 0,
        tags=data.get("tags", []),
        description=(data.get("description", "") or "")[:500],
        chapters=[{"start_time": c.get("start_time",0), "end_time": c.get("end_time",0), "title": c.get("title","")} for c in (data.get("chapters") or [])],
    )

def get_video_subtitles(url: str, langs: List[str] = None) -> Optional[TranscriptResult]:
    """使用 yt-dlp 获取平台字幕"""
    if langs is None:
        langs = ["zh-Hans", "zh", "en"]
    print(f"[info] 尝试获取字幕 ({','.join(langs)})...", file=sys.stderr)
    tmpdir = tempfile.mkdtemp()
    cmd = yt_dlp_args() + ["--write-subs", "--write-auto-sub", f"--sub-langs={','.join(langs)}",
           "--sub-format=srt/vtt/best", f"--output={tmpdir}/%(id)s.%(ext)s", "--skip-download"]
    result = run_command(cmd + [url], timeout=90, env=command_env())

    subtitle_files = sorted(os.listdir(tmpdir), key=lambda name: (not name.endswith(".srt"), name))
    for f in subtitle_files:
        if f.endswith((".srt", ".vtt")):
            subtitle_path = os.path.join(tmpdir, f)
            with open(subtitle_path, "r", encoding="utf-8", errors="ignore") as sf:
                text = sf.read()
            segments = parse_srt(text) if f.endswith(".srt") else parse_vtt(text)
            if segments:
                return TranscriptResult(
                    language="zh",
                    full_text="\n".join(s.text for s in segments),
                    segments=segments
                )
    if result.returncode != 0:
        print(f"[info] 字幕获取失败: {result.stderr[:200]}", file=sys.stderr)
    return None

def download_audio(url: str, output_dir: str, platform: str) -> Optional[AudioMeta]:
    """使用 yt-dlp 下载音频，或在本地文件模式下直接返回原文件。"""
    os.makedirs(output_dir, exist_ok=True)
    if platform == "local" and os.path.isfile(url):
        return AudioMeta(
            video_id=os.path.splitext(os.path.basename(url))[0],
            title=os.path.splitext(os.path.basename(url))[0],
            duration=probe_media_duration(url),
            platform=platform,
            file_path=os.path.abspath(url),
        )
    output_template = os.path.join(output_dir, "%(id)s.%(ext)s")
    cmd = yt_dlp_args() + ["-f", "bestaudio[ext=m4a]/bestaudio/best", "-o", output_template,
           "--no-playlist", "--postprocessor-args", "ffmpeg:-b:a 64k"]
    print(f"[download] 正在下载音频...", file=sys.stderr)
    result = run_command(cmd + [url], timeout=600, env=command_env())
    if result.returncode != 0:
        print(f"[error] 音频下载失败: {result.stderr[:200]}", file=sys.stderr)
        if platform == "bilibili":
            fallback = download_bilibili_via_api(url, output_dir)
            if fallback:
                print(f"[bilibili-api] fallback 成功: {fallback.file_path}", file=sys.stderr)
                return fallback
        return None

    for f in os.listdir(output_dir):
        if f.endswith((".m4a", ".mp3", ".wav", ".ogg", ".webm")):
            video_id = f.rsplit(".", 1)[0]
            json_file = os.path.join(output_dir, f.rsplit(".", 1)[0] + ".info.json")
            title = video_id
            duration = 0
            if os.path.exists(json_file):
                with open(json_file, "r", encoding="utf-8") as jf:
                    jdata = json.load(jf)
                    title = jdata.get("title", video_id)
                    duration = parse_duration(jdata.get("duration", 0))
            return AudioMeta(video_id=video_id, title=title, duration=duration,
                            platform=platform, file_path=os.path.join(output_dir, f))
    return None


def download_video_for_frames(url: str, output_dir: str, platform: str) -> Optional[str]:
    if platform == "local" and os.path.isfile(url):
        return url

    frame_source_dir = os.path.join(output_dir, "visual_source_h264")
    os.makedirs(frame_source_dir, exist_ok=True)
    output_template = os.path.join(frame_source_dir, "%(id)s.%(ext)s")
    cmd = yt_dlp_args() + [
        "-f", "bestvideo[vcodec^=avc1][height<=720]+bestaudio/bestvideo[vcodec!=av01][height<=720]+bestaudio/best[height<=720]/best",
        "-o", output_template,
        "--no-playlist",
        "--merge-output-format", "mp4",
    ]
    print("[vision] 正在下载视频用于抽帧...", file=sys.stderr)
    result = run_command(cmd + [url], timeout=900, env=command_env())
    if result.returncode != 0:
        print(f"[vision] 视频下载失败: {result.stderr[:200]}", file=sys.stderr)
        if platform == "bilibili":
            fallback = download_bilibili_via_api(url, output_dir)
            if fallback:
                print(f"[vision] 使用 Bilibili API fallback 视频抽帧: {fallback.file_path}", file=sys.stderr)
                return fallback.file_path
        print("[vision] 无法抽帧", file=sys.stderr)
        return None

    video_exts = (".mp4", ".mkv", ".webm", ".mov", ".flv", ".avi", ".m4v")
    candidates = [
        os.path.join(frame_source_dir, name)
        for name in os.listdir(frame_source_dir)
        if name.lower().endswith(video_exts)
    ]
    if not candidates:
        return None
    return max(candidates, key=os.path.getmtime)


def extract_visual_frames(video_path: str, output_dir: str, safe_id: str, duration: float,
                          segments: List[dict], frame_interval: float = 30.0,
                          max_frames: int = 8) -> List[FrameInfo]:
    if not video_path or not os.path.exists(video_path):
        return []

    frames_dir = os.path.join(output_dir, f"{safe_id}_frames")
    os.makedirs(frames_dir, exist_ok=True)

    duration = float(duration or 0) or probe_media_duration(video_path)
    frame_interval = max(1.0, float(frame_interval or 30.0))
    max_frames = min(MAX_AGENT_FRAMES, max(1, int(max_frames or 8)))

    if duration > 0:
        # Prefer representative key frames across the whole video. The old interval-only
        # behavior often produced only the opening seconds when max_frames was small,
        # which caused agents to forget meaningful visual evidence.
        if max_frames <= 1:
            fractions = [0.5]
        elif max_frames == 2:
            fractions = [0.25, 0.75]
        elif max_frames == 3:
            fractions = [0.20, 0.50, 0.80]
        else:
            fractions = [(i + 1) / (max_frames + 1) for i in range(max_frames)]
        timestamps = [min(max(1.0, duration * frac), max(1.0, duration - 1.0)) for frac in fractions]
    else:
        timestamps = [i * frame_interval for i in range(max_frames)]

    frames = []
    for index, timestamp in enumerate(timestamps, start=1):
        image_path = os.path.join(frames_dir, f"frame_{index:03d}_{int(timestamp):06d}s.jpg")
        cmd = [
            FFMPEG, "-y",
            "-ss", f"{timestamp:.3f}",
            "-i", video_path,
            "-frames:v", "1",
            "-vf", f"scale=min({FRAME_MAX_WIDTH}\\,iw):-2",
            "-q:v", "7",
            image_path,
        ]
        result = run_command(cmd, timeout=120, env=command_env())
        if result.returncode != 0 or not os.path.exists(image_path):
            print(f"[vision] 抽帧失败 {format_timestamp(timestamp)}: {result.stderr[:160]}", file=sys.stderr)
            continue
        frames.append(FrameInfo(
            index=index,
            timestamp=timestamp,
            timestamp_text=format_timestamp(timestamp),
            image_path=os.path.abspath(image_path),
            nearby_transcript=find_nearby_transcript(segments, timestamp),
            visual_note="",
        ))

    if frames:
        print(f"[vision] 已抽取视觉帧: {len(frames)} 张", file=sys.stderr)
    return frames


def build_notes_markdown(output: TranscribeOutput, safe_id: str) -> str:
    info = output.video_info or {}
    title = info.get("title") or safe_id
    uploader = info.get("uploader") or ""
    duration = format_timestamp(float(info.get("duration") or 0))
    tags = info.get("tags") or []
    source = output.source or "unknown"

    safe_title = str(title).replace('"', "'")
    lines = [
        "```mermaid",
        "flowchart LR",
        f"  V[\"{safe_title}\"] --> A[\"核心观点\"]",
        "  V --> B[\"关键证据/案例\"]",
        "  V --> C[\"方法/步骤\"]",
        "  V --> D[\"风险与限制\"]",
        "  V --> E[\"视觉证据/关键帧\"]",
        "```",
        "",
        f"# {title}",
        "",
        "## 基本信息",
        "",
        f"- 来源：{source}",
        f"- UP 主/作者：{uploader}" if uploader else "- UP 主/作者：未知",
        f"- 时长：{duration}",
    ]
    if tags:
        lines.append(f"- 标签：{', '.join(str(tag) for tag in tags)}")
    if output.visual_frames:
        lines.append(f"- 视觉帧：{len(output.visual_frames)} 张（已抽取并嵌入 Markdown；仍需模型逐帧补充真实视觉观察）")
    if output.chunk_summaries_file:
        lines.append(f"- 分块摘要：`{output.chunk_summaries_file}`")
    lines.extend(["", "## 一句话总结", ""])

    if output.transcript_text:
        first_text = " ".join(output.transcript_text.split())[:180]
        lines.append(first_text + ("……" if len(output.transcript_text) > 180 else ""))
    else:
        lines.append("该视频暂无可用转写文本，请结合视觉帧和元信息继续分析。")

    lines.extend(["", "## 时间线与视觉证据", ""])
    if output.visual_frames:
        for frame in output.visual_frames:
            ts = frame.get("timestamp_text", "00:00")
            image_path = frame.get("image_path", "")
            nearby = frame.get("nearby_transcript", "").strip()
            visual_note = frame.get("visual_note", "").strip()
            rel_path = image_path
            try:
                rel_path = os.path.relpath(image_path, os.path.dirname(output.output_file))
            except Exception:
                pass
            rel_path = rel_path.replace(os.sep, "/")
            lines.extend([
                f"### {ts}",
                "",
                f"![视频截图 {ts}]({rel_path})" if image_path else "",
                "",
                f"*Frame path: `{rel_path}`*" if image_path else "",
                "",
            ])
            if visual_note:
                lines.extend([f"**视觉观察**：{visual_note}", ""])
            else:
                lines.extend(["**视觉观察**：pending visual review — 必须由多模态模型读取该帧后补充；若模型不支持图片输入，可使用 OCR fallback 并标注来源。", ""])
            if nearby:
                lines.extend([f"**附近转写**：{nearby}", ""])
    elif output.segments:
        for segment in output.segments[:12]:
            ts = format_timestamp(float(segment.get("start", 0) or 0))
            text = str(segment.get("text", "")).strip()
            if text:
                lines.append(f"- `{ts}` {text}")
        lines.append("")
    else:
        lines.append("暂无时间线数据。")
        lines.append("")

    lines.extend(["## 结构化摘要", ""])
    if output.segments:
        chunk_size = max(1, len(output.segments) // 5)
        for i in range(0, len(output.segments), chunk_size):
            chunk = output.segments[i:i + chunk_size]
            start = format_timestamp(float(chunk[0].get("start", 0) or 0))
            text = " ".join(str(s.get("text", "")).strip() for s in chunk if str(s.get("text", "")).strip())[:260]
            if text:
                lines.append(f"- `{start}` {text}")
    else:
        lines.append("- 暂无字幕/转写内容。")

    lines.extend(["", "## 转写预览", ""])
    if output.transcript_text:
        lines.append(compact_text(output.transcript_text, NOTES_TRANSCRIPT_PREVIEW_CHARS))
        lines.append("")
        lines.append("完整转写仅保存在结构化 JSON 中。为了避免 Claude Code 上下文溢出，默认不要整文件读取；先读分块摘要。")
    else:
        lines.append("暂无完整转写。")

    if output.visual_manifest_file:
        lines.extend(["", "## 关联文件", "", f"- 视觉清单：`{output.visual_manifest_file}`"])
    if output.chunk_summaries_file:
        lines.append(f"- 分块摘要：`{output.chunk_summaries_file}`")
    if output.final_notes_file:
        lines.append(f"- 最终笔记：`{output.final_notes_file}`")
    if output.output_file:
        lines.append(f"- 结构化数据：`{output.output_file}`")

    return "\n".join(line for line in lines if line is not None).rstrip() + "\n"

# ============================================================
# 主流程
# ============================================================

def generate_transcript(url: str, output_dir: str = "./notes",
                        prefer_subtitle: bool = True, force_transcribe: bool = False,
                        extract_frames: bool = False, frame_interval: float = 30.0,
                        max_frames: int = 8) -> TranscribeOutput:
    """
    视频→转写 主流程
    - 自动检测平台
    - 优先获取字幕
    - 字幕不可用时下载音频 + whisper.cpp/faster-whisper 转写
    - 可选下载视频并用 ffmpeg 抽帧，输出供多模态模型原生读图的视觉清单
    - 输出结构化 JSON 供 Agent 生成笔记
    """
    issues = check_deps()
    if issues:
        print("[ERROR] 缺少必要依赖:", file=sys.stderr)
        for issue in issues:
            print(f"  - {issue}", file=sys.stderr)
        sys.exit(1)

    # 平台检测
    url_lower = url.lower()
    if 'bilibili.com' in url_lower or 'b23.tv' in url_lower:
        platform = 'bilibili'
    elif 'youtube.com' in url_lower or 'youtu.be' in url_lower:
        platform = 'youtube'
    elif 'douyin.com' in url_lower:
        platform = 'douyin'
    elif 'kuaishou.com' in url_lower:
        platform = 'kuaishou'
    elif os.path.exists(url):
        platform = 'local'
    else:
        platform = 'unknown'

    if platform == 'unknown':
        raise ValueError(f"无法识别平台: {url}")

    video_id = ""
    if platform == "bilibili":
        m = re.search(r"BV([0-9A-Za-z]+)", url)
        video_id = f"BV{m.group(1)}" if m else "unknown"
    elif platform == "youtube":
        m = re.search(r"(?:v=|youtu\.be/)([0-9A-Za-z_-]{11})", url)
        video_id = m.group(1) if m else "unknown"
    else:
        video_id = url.split("/")[-1].split("?")[0][:50]

    print(f"[info] 平台: {platform} | 视频: {video_id}", file=sys.stderr)

    # 获取视频信息
    video_info_obj = get_video_info(url, platform)
    os.makedirs(output_dir, exist_ok=True)

    output = TranscribeOutput(
        video_info={
            "title": video_info_obj.title,
            "uploader": video_info_obj.uploader,
            "duration": video_info_obj.duration,
            "view_count": video_info_obj.view_count,
            "like_count": video_info_obj.like_count,
            "tags": video_info_obj.tags,
            "description": video_info_obj.description,
            "chapters": video_info_obj.chapters,
        },
        transcript_text="",
        source="metadata",
    )

    # 1. 尝试字幕优先 (B站等)
    if prefer_subtitle and platform in ("bilibili", "youtube"):
        transcript = get_video_subtitles(url)
        if transcript and transcript.segments:
            print(f"[info] 字幕获取成功: {len(transcript.segments)} 段", file=sys.stderr)
            output.transcript_text = transcript.full_text
            output.segments = [asdict(s) for s in transcript.segments]
            output.source = "subtitle"

    # 2. 字幕不可用 或 force_transcribe → 下载音频 + whisper.cpp
    if not output.transcript_text:
        print("[info] 字幕不可用，尝试下载音频...", file=sys.stderr)
        audio_meta = download_audio(url, output_dir, platform)
        if audio_meta:
            print(f"[info] 音频下载完成: {os.path.basename(audio_meta.file_path)} ({audio_meta.duration:.0f}s)", file=sys.stderr)

            if force_transcribe or TRANSCRIBER_TYPE == "faster-whisper" or get_whisper_cpp() or os.getenv("WHISPER_CPP"):
                if TRANSCRIBER_TYPE == "faster-whisper" and not os.getenv("WHISPER_CPP"):
                    whisper_segments = transcribe_via_faster_whisper(audio_meta.file_path, WHISPER_MODEL)
                else:
                    whisper_segments = transcribe_via_whisper_cpp(audio_meta.file_path, WHISPER_MODEL)
                if whisper_segments:
                    output.transcript_text = "\n".join(s.text for s in whisper_segments)
                    output.segments = [asdict(s) for s in whisper_segments]
                    output.source = TRANSCRIBER_TYPE if TRANSCRIBER_TYPE == "faster-whisper" else "whisper.cpp"
                else:
                    output.source = "audio_only"
                    output.source_note = f"音频已保存到: {audio_meta.file_path}，转写器未产出文本。"
            else:
                output.source = "audio_only"
                output.source_note = f"音频已保存到: {audio_meta.file_path}，配置转写器后可自动转写。"
        else:
            output.source = "failed"

    # 保存 JSON
    safe_id = re.sub(r'[^\w-]', '', video_id)[:50]

    if extract_frames:
        video_path = download_video_for_frames(url, output_dir, platform)
        frames = extract_visual_frames(
            video_path=video_path,
            output_dir=output_dir,
            safe_id=safe_id,
            duration=video_info_obj.duration,
            segments=output.segments,
            frame_interval=frame_interval,
            max_frames=max_frames,
        )
        output.visual_frames = [asdict(frame) for frame in frames]
        if output.visual_frames:
            output.visual_manifest_file = os.path.join(output_dir, f"{safe_id}_visual_manifest.json")
            with open(output.visual_manifest_file, "w", encoding="utf-8") as f:
                json.dump({
                    "video_info": output.video_info,
                    "frames": output.visual_frames,
                    "agent_read_policy": {
                        "text_first": True,
                        "max_images_per_model_request": 1,
                        "default_image_action": "Do not open images unless visual evidence is required.",
                        "fallback": "If image input is unavailable or context is tight, use timestamp and nearby_transcript only."
                    },
                    "instruction": "Use native multimodal image understanding only one frame at a time. Never send all frames plus transcript together. If image input is unavailable, use OCR only as fallback and label it OCR-derived.",
                }, f, ensure_ascii=False, indent=2)

    output_file = os.path.join(output_dir, f"{safe_id}_transcript.json")
    chunk_summaries_file = os.path.join(output_dir, f"{safe_id}_chunk_summaries.md")
    final_notes_file = os.path.join(output_dir, f"{safe_id}_final_notes.md")

    output.output_file = output_file
    output.chunk_summaries_file = chunk_summaries_file
    output.final_notes_file = final_notes_file
    chunk_summaries_md = build_chunk_summaries_markdown(output, safe_id)
    with open(chunk_summaries_file, "w", encoding="utf-8") as f:
        f.write(chunk_summaries_md)

    output.notes_md = build_notes_markdown(output, safe_id)
    notes_file = os.path.join(output_dir, f"{safe_id}_notes.md")
    with open(notes_file, "w", encoding="utf-8") as f:
        f.write(output.notes_md)
    with open(final_notes_file, "w", encoding="utf-8") as f:
        f.write(output.notes_md)

    output_data = asdict(output)
    output_data["notes_file"] = notes_file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*60}", file=sys.stderr)
    print(f"  转写完成！", file=sys.stderr)
    print(f"{'='*60}", file=sys.stderr)
    print(f"  视频: {video_info_obj.title}", file=sys.stderr)
    print(f"  上传者: {video_info_obj.uploader}", file=sys.stderr)
    print(f"  时长: {timedelta(seconds=int(video_info_obj.duration))}", file=sys.stderr)
    print(f"  观看: {video_info_obj.view_count:,}", file=sys.stderr)
    print(f"  信息来源: {output.source}", file=sys.stderr)
    if output.segments:
        print(f"  段落数: {len(output.segments)}", file=sys.stderr)
        print(f"  分块摘要: {chunk_summaries_file}", file=sys.stderr)
    print(f"  输出: {output_file}", file=sys.stderr)
    print(f"  笔记: {notes_file}", file=sys.stderr)
    print(f"  最终笔记: {final_notes_file}", file=sys.stderr)
    print(f"{'='*60}", file=sys.stderr)
    return output

def main():
    parser = argparse.ArgumentParser(
        description="Video Notes Generator — 视频转录 (零pip依赖，支持whisper.cpp自动编译)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s "https://www.bilibili.com/video/BV1xxxxx"
  %(prog)s "https://www.bilibili.com/video/BV1xxxxx" -o ./my_notes/
  %(prog)s "视频URL" --transcribe --model base
  %(prog)s "/path/to/local/video.mp4"

环境变量:
  WHISPER_CPP    whisper.cpp 二进制路径 (默认自动查找)
  WHISPER_MODEL  转写模型 (默认: base, 可选: tiny/base/small/medium/large-v3/large-v3-turbo 或自定义映射)
  VIDEO_NOTES_PROXY  显式代理 URL；未设置时回退 config/proxy.json 与 HTTP_PROXY/HTTPS_PROXY
  VIDEO_NOTES_WHISPER_MODEL_CONFIG  自定义 faster-whisper 模型映射 JSON
        """
    )
    parser.add_argument("url", help="视频 URL (Bilibili/YouTube/抖音) 或本地文件路径")
    parser.add_argument("-o", "--output", default="./notes", help="输出目录 (默认: ./notes)")
    parser.add_argument("--no-subtitle", action="store_true", help="跳过字幕获取，直接下载音频")
    parser.add_argument("--transcribe", action="store_true", help="强制使用 whisper.cpp 转写")
    parser.add_argument("--model", default=None, help="whisper.cpp 模型 (默认读取 WHISPER_MODEL 环境变量或 base)")
    parser.add_argument("--frames", action="store_true", help="兼容旧参数：抽帧现在默认启用")
    parser.add_argument("--no-frames", action="store_true", help="紧急文本-only模式：跳过抽帧/附图；必须在最终报告中说明原因")
    parser.add_argument("--frame-interval", type=float, default=30.0, help="抽帧间隔秒数，默认 30")
    parser.add_argument("--max-frames", type=int, default=MAX_AGENT_FRAMES, help=f"最多抽取帧数，默认 {MAX_AGENT_FRAMES}")
    parser.add_argument("--print-full-json", action="store_true", help="危险：在 stdout 打印完整 JSON。默认只打印短摘要，避免 Claude Code 上下文溢出")
    args = parser.parse_args()

    global WHISPER_MODEL
    if args.model:
        WHISPER_MODEL = args.model

    try:
        output = generate_transcript(
            url=args.url,
            output_dir=args.output,
            prefer_subtitle=not args.no_subtitle,
            force_transcribe=args.transcribe,
            extract_frames=not args.no_frames,
            frame_interval=args.frame_interval,
            max_frames=args.max_frames,
        )
        if args.print_full_json:
            print(json.dumps(asdict(output), ensure_ascii=False, indent=2))
        else:
            print(json.dumps({
                "ok": True,
                "source": output.source,
                "segment_count": len(output.segments),
                "frame_count": len(output.visual_frames),
                "transcript_json": output.output_file,
                "chunk_summaries": output.chunk_summaries_file,
                "final_notes": output.final_notes_file,
                "visual_manifest": output.visual_manifest_file,
                "read_policy": "Read final_notes and chunk_summaries first. For video summaries, inspect representative frames one at a time and replace pending visual notes with native multimodal observations when available.",
            }, ensure_ascii=False, indent=2))
        return 0
    except Exception as e:
        print(f"\n[error] 失败: {e}", file=sys.stderr)
        import traceback; traceback.print_exc(file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
