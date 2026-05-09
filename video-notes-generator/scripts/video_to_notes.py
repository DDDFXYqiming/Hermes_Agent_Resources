#!/usr/bin/env python3
"""
Video Notes Generator — 核心脚本 (零pip依赖版本)
依赖: yt-dlp (二进制), ffmpeg (系统包)
无需安装任何 Python 扩展包。whisper.cpp 可选，有则自动转写。

用法:
    python3 video_to_notes.py <video_url> [--output ./notes]
    python3 video_to_notes.py <video_url> --transcribe --model base
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import asdict, dataclass, field
from datetime import timedelta
from typing import List, Optional

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
class TranscribeOutput:
    video_info: dict = field(default_factory=dict)
    transcript_text: str = ""
    segments: List[dict] = field(default_factory=list)
    chapters: List[dict] = field(default_factory=list)
    source: str = ""
    output_file: str = ""
    notes_md: str = ""  # 由 Agent 填充的 Markdown 笔记

# ============================================================
# 工具函数
# ============================================================

YTDLP = shutil.which("yt-dlp") or os.path.expanduser("~/.local/bin/yt-dlp")
FFMPEG = shutil.which("ffmpeg") or "ffmpeg"

WHISPER_CPP_PATH = os.getenv("WHISPER_CPP", "")
WHISPER_MODEL = os.getenv("WHISPER_MODEL", "base").lower()

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
    if not shutil.which(FFMPEG):
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

# ============================================================
# 视频信息 + 字幕获取
# ============================================================

def get_video_info(url: str, platform: str) -> VideoInfo:
    print(f"[info] 获取视频元数据...", file=sys.stderr)
    cmd = [YTDLP, "--dump-json", "--no-playlist", "--skip-download"]
    env = {**os.environ, "PATH": f"{os.path.expanduser('~/.local/bin')}:{os.environ.get('PATH', '')}"}
    result = subprocess.run(cmd + [url], capture_output=True, text=True, timeout=60, env=env)

    if result.returncode != 0:
        return VideoInfo(video_url=url, video_id=url.split("/")[-1][:50], platform=platform)
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
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
    cmd = [YTDLP, "--write-subs", "--write-auto-sub", f"--sub-langs={','.join(langs)}",
           "--sub-format=srt", f"--output={tmpdir}/%(id)s.%(ext)s", "--skip-download"]
    env = {**os.environ, "PATH": f"{os.path.expanduser('~/.local/bin')}:{os.environ.get('PATH', '')}"}
    result = subprocess.run(cmd + [url], capture_output=True, text=True, timeout=60, env=env)

    for f in os.listdir(tmpdir):
        if f.endswith(".srt"):
            srt_path = os.path.join(tmpdir, f)
            with open(srt_path, "r", encoding="utf-8", errors="ignore") as sf:
                segments = parse_srt(sf.read())
            if segments:
                return TranscriptResult(
                    language="zh",
                    full_text="\n".join(s.text for s in segments),
                    segments=segments
                )
    return None

def download_audio(url: str, output_dir: str, platform: str) -> Optional[AudioMeta]:
    """使用 yt-dlp 下载音频"""
    os.makedirs(output_dir, exist_ok=True)
    output_template = os.path.join(output_dir, "%(id)s.%(ext)s")
    cmd = [YTDLP, "-f", "bestaudio[ext=m4a]/bestaudio/best", "-o", output_template,
           "--no-playlist", "--postprocessor-args", "ffmpeg:-b:a 64k"]
    env = {**os.environ, "PATH": f"{os.path.expanduser('~/.local/bin')}:{os.environ.get('PATH', '')}"}
    print(f"[download] 正在下载音频...", file=sys.stderr)
    result = subprocess.run(cmd + [url], capture_output=True, text=True, timeout=600, env=env)
    if result.returncode != 0:
        print(f"[error] 音频下载失败: {result.stderr[:200]}", file=sys.stderr)
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

# ============================================================
# 主流程
# ============================================================

def generate_transcript(url: str, output_dir: str = "./notes",
                        prefer_subtitle: bool = True, force_transcribe: bool = False) -> TranscribeOutput:
    """
    视频→转写 主流程
    - 自动检测平台
    - 优先获取字幕
    - 字幕不可用时下载音频 + whisper.cpp 转写
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

            if force_transcribe or get_whisper_cpp() or os.getenv("WHISPER_CPP"):
                whisper_segments = transcribe_via_whisper_cpp(audio_meta.file_path, WHISPER_MODEL)
                if whisper_segments:
                    output.transcript_text = "\n".join(s.text for s in whisper_segments)
                    output.segments = [asdict(s) for s in whisper_segments]
                    output.source = "audio_transcription"
                else:
                    output.source = "audio_only"
                    output.source_note = f"需 whisper.cpp 转写，音频: {audio_meta.file_path}"
            else:
                output.source = "audio_only"
                output.source_note = f"音频已保存至: {audio_meta.file_path}。安装 whisper.cpp 可自动转写。"
        else:
            output.source = "failed"

    # 保存 JSON
    safe_id = re.sub(r'[^\w-]', '', video_id)[:50]
    output_file = os.path.join(output_dir, f"{safe_id}_transcript.json")

    output.output_file = output_file
    output_data = asdict(output)
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
    print(f"  输出: {output_file}", file=sys.stderr)
    print(f"{'='*60}", file=sys.stderr)
    return output

def main():
    parser = argparse.ArgumentParser(
        description="Video Notes Generator — 视频转录 (零pip依赖，支持whisper.cpp自动编译)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s "https://www.bilibili.com/video/BV1TfRfBJEZw"
  %(prog)s "https://www.bilibili.com/video/BV1TfRfBJEZw" -o ./my_notes/
  %(prog)s "视频URL" --transcribe --model base
  %(prog)s "/path/to/local/video.mp4"

环境变量:
  WHISPER_CPP    whisper.cpp 二进制路径 (默认自动查找)
  WHISPER_MODEL  转写模型 (默认: base, 可选: tiny, small, medium)
        """
    )
    parser.add_argument("url", help="视频 URL (Bilibili/YouTube/抖音) 或本地文件路径")
    parser.add_argument("-o", "--output", default="./notes", help="输出目录 (默认: ./notes)")
    parser.add_argument("--no-subtitle", action="store_true", help="跳过字幕获取，直接下载音频")
    parser.add_argument("--transcribe", action="store_true", help="强制使用 whisper.cpp 转写")
    parser.add_argument("--model", default=None, help="whisper.cpp 模型 (默认读取 WHISPER_MODEL 环境变量或 base)")
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
        )
        print(json.dumps(asdict(output), ensure_ascii=False, indent=2))
        return 0
    except Exception as e:
        print(f"\n[error] 失败: {e}", file=sys.stderr)
        import traceback; traceback.print_exc(file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())