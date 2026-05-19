#!/usr/bin/env python3
import importlib.util
import json
import platform
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from ga_env import add_generic_agent_paths, env_status  # noqa: E402


def has_module(name):
    try:
        return importlib.util.find_spec(name) is not None
    except Exception:
        return False


def get_screen_size():
    if platform.system().lower() == "windows":
        try:
            import ctypes
            user32 = ctypes.windll.user32
            try:
                user32.SetProcessDPIAware()
            except Exception:
                pass
            return [int(user32.GetSystemMetrics(0)), int(user32.GetSystemMetrics(1))]
        except Exception:
            pass
    try:
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        size = [root.winfo_screenwidth(), root.winfo_screenheight()]
        root.destroy()
        return size
    except Exception:
        return None


def main():
    ga_root, added_paths = add_generic_agent_paths()
    deps = {name: has_module(name) for name in [
        "win32gui", "win32api", "win32con", "win32process",
        "PIL", "pyperclip", "uiautomation", "pyautogui", "cv2", "numpy",
        "simple_websocket_server",
    ]}
    ga_files = None
    if ga_root:
        ga_files = {
            "root_exists": ga_root.exists(),
            "ga.py": (ga_root / "ga.py").exists(),
            "ljqCtrl.py": (ga_root / "memory" / "ljqCtrl.py").exists(),
            "ocr_utils.py": (ga_root / "memory" / "ocr_utils.py").exists(),
            "TMWebDriver.py": (ga_root / "TMWebDriver.py").exists(),
            "tmwd_cdp_bridge": (ga_root / "assets" / "tmwd_cdp_bridge").exists(),
        }
    result = {
        "ok": True,
        "action": "desktop_probe",
        "python": sys.executable,
        "platform": platform.platform(),
        "cwd": str(Path.cwd()),
        "screen": get_screen_size(),
        "deps": deps,
        "environment": env_status(ga_root),
        "added_paths": added_paths,
        "generic_agent_files": ga_files,
        "note": None if ga_root else "GENERIC_AGENT_ROOT is not set and no GenericAgent root was discovered; GenericAgent-specific modules will be unavailable.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
