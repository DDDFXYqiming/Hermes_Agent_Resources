#!/usr/bin/env python3
import argparse
import json
import sys
import traceback


def list_windows(find_title=None):
    import win32gui
    rows = []

    def cb(hwnd, _):
        if not win32gui.IsWindowVisible(hwnd):
            return
        title = win32gui.GetWindowText(hwnd)
        if not title:
            return
        if find_title and find_title.lower() not in title.lower():
            return
        item = {
            "hwnd": hwnd,
            "title": title,
            "class": win32gui.GetClassName(hwnd),
            "rect": list(win32gui.GetWindowRect(hwnd)),
        }
        rows.append(item)

    win32gui.EnumWindows(cb, None)
    return rows


def hwnd_rect(hwnd):
    import win32gui
    return {
        "hwnd": hwnd,
        "title": win32gui.GetWindowText(hwnd),
        "class": win32gui.GetClassName(hwnd),
        "rect": list(win32gui.GetWindowRect(hwnd)),
        "visible": bool(win32gui.IsWindowVisible(hwnd)),
    }


def main():
    ap = argparse.ArgumentParser(description="GenericAgent-style safe window observation helpers")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--find-title")
    ap.add_argument("--hwnd", type=int)
    ap.add_argument("--rect", action="store_true")
    args = ap.parse_args()

    try:
        if args.hwnd and args.rect:
            payload = {"ok": True, "action": "hwnd_rect", "window": hwnd_rect(args.hwnd)}
        else:
            payload = {"ok": True, "action": "list_windows", "windows": list_windows(args.find_title)}
    except Exception as e:
        payload = {
            "ok": False,
            "action": "window_ops",
            "error": {"type": type(e).__name__, "message": str(e), "traceback": traceback.format_exc()},
        }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
