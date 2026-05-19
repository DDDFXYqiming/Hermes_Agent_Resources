#!/usr/bin/env python3
import argparse
import json
import os
import subprocess
import sys
import time
import traceback
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from ga_env import add_generic_agent_paths, env_status, find_worker_python  # noqa: E402


def should_reexec_with_worker_python():
    target = find_worker_python()
    if not target:
        return False
    try:
        return Path(sys.executable).resolve() != target.resolve() and "--_worker" not in sys.argv
    except Exception:
        return "--_worker" not in sys.argv


def reexec_with_worker_python():
    target = find_worker_python()
    args = [str(target), __file__, "--_worker"] + sys.argv[1:]
    cp = subprocess.run(args, text=True, capture_output=True, timeout=60)
    if cp.stdout:
        print(cp.stdout, end="")
    if cp.stderr:
        print(cp.stderr, file=sys.stderr, end="")
    raise SystemExit(cp.returncode)


def default_out_dir():
    base = os.environ.get("HERMES_HOME") or str(Path.home() / ".hermes")
    out = Path(base) / "temp" / "generic_agent_code_run" / "screenshots"
    out.mkdir(parents=True, exist_ok=True)
    return out


def capture(args):
    from PIL import ImageGrab
    bbox = None
    if args.bbox:
        bbox = tuple(args.bbox)
    elif args.hwnd:
        import win32gui
        bbox = tuple(win32gui.GetWindowRect(args.hwnd))
    image = ImageGrab.grab(bbox=bbox)
    out_path = Path(args.out) if args.out else default_out_dir() / f"screen_{int(time.time()*1000)}.png"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(out_path)
    return out_path, image.size


def try_ocr(image_path):
    try:
        import pytesseract
        from PIL import Image
        return {"available": True, "text": pytesseract.image_to_string(Image.open(image_path))}
    except Exception as e:
        return {"available": False, "text": "", "error": f"{type(e).__name__}: {e}"}


def main():
    ap = argparse.ArgumentParser(description="GenericAgent-style screenshot and optional OCR helper")
    ap.add_argument("--_worker", action="store_true", help=argparse.SUPPRESS)
    ap.add_argument("--screen", action="store_true")
    ap.add_argument("--bbox", nargs=4, type=int)
    ap.add_argument("--hwnd", type=int)
    ap.add_argument("--image")
    ap.add_argument("--ocr", action="store_true")
    ap.add_argument("--out")
    args = ap.parse_args()

    add_generic_agent_paths()
    if should_reexec_with_worker_python():
        reexec_with_worker_python()

    try:
        if args.image:
            image_path = Path(args.image)
            size = None
        else:
            image_path, size = capture(args)
        evidence = {"image_path": str(image_path), "size": size, "python": sys.executable, "environment": env_status()}
        if args.ocr:
            evidence["ocr"] = try_ocr(image_path)
        payload = {"ok": True, "action": "screenshot_ocr", "evidence": evidence}
    except Exception as e:
        payload = {
            "ok": False,
            "action": "screenshot_ocr",
            "environment": env_status(),
            "error": {"type": type(e).__name__, "message": str(e), "traceback": traceback.format_exc()},
            "hint": "Install Pillow/pywin32 in the current Python, or set GENERIC_AGENT_PYTHON to a Python executable with those dependencies, or set GENERIC_AGENT_ROOT to a checkout that has .venv/venv.",
        }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
