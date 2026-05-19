# Windows Control

Use GenericAgent-style `code_run` to call Windows local automation libraries on demand.

## Source Files

The exact GenericAgent location is environment-specific. Configure `GENERIC_AGENT_ROOT` first, then refer to files relative to that root:

- `%GENERIC_AGENT_ROOT%\memory\ljqCtrl.py`
- `%GENERIC_AGENT_ROOT%\memory\ocr_utils.py`
- `%GENERIC_AGENT_ROOT%\memory\ui_detect.py`
- `%GENERIC_AGENT_ROOT%\memory\cloakbrowser_sop.md`
- `%GENERIC_AGENT_ROOT%\memory\qq_sop.md`

See `references/environment.md` for portable setup.

## Capability Map

| Need | API / Library |
|---|---|
| enumerate windows | `win32gui.EnumWindows` |
| target verification | `GetWindowText`, `GetClassName`, `GetWindowRect` |
| activate window | `ShowWindow`, `SetForegroundWindow` |
| screen capture | `PIL.ImageGrab.grab` |
| background/window capture fallback | `PrintWindow` |
| OCR | `ocr_utils`, PaddleOCR, Tesseract, RapidOCR |
| UI tree | `uiautomation`, `pywinauto` |
| mouse | `win32api.SetCursorPos`, `mouse_event` |
| keyboard | `win32api.keybd_event` |
| Chinese input | `pyperclip.copy` + paste hotkey |

## Minimal Window Observation Snippet

```python
import json, win32gui
windows = []
def cb(hwnd, _):
    if win32gui.IsWindowVisible(hwnd):
        title = win32gui.GetWindowText(hwnd)
        if title:
            windows.append({
                "hwnd": hwnd,
                "title": title,
                "class": win32gui.GetClassName(hwnd),
                "rect": win32gui.GetWindowRect(hwnd),
            })
win32gui.EnumWindows(cb, None)
print(json.dumps({"ok": True, "action": "list_windows", "windows": windows}, ensure_ascii=False))
```

## Operating Rule

Do not click until target window and target element are observed. After clicking or typing, immediately verify with screenshot/OCR/UIA/window state.
