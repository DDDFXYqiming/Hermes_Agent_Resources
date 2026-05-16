---
name: generic-agent-code-run
description: "Use when controlling Windows native desktop apps or real-browser sessions with GenericAgent-style code_run: dynamic Python execution, Win32/UIA/OCR/screenshots/CDP, and observe-act-verify loops."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [genericagent, code-run, windows, desktop-automation, win32, uia, ocr, cdp]
    related_skills: [hermes-agent, hermes-agent-skill-authoring, systematic-debugging]
---

# GenericAgent Code_Run

## Overview

Use this skill to operate Windows native desktop apps and real-browser sessions with the GenericAgent pattern: minimal fixed tools, a universal `code_run` execution path, local capability libraries, and a strict observe-act-verify loop.

The core idea is not to memorize many fixed tools. The core idea is to generate short, task-specific Python code, execute it, return JSON evidence, and decide the next action from verified state.

## When to Use

Use this skill when a task needs:

- Windows native app control: window enumeration, activation, screenshots, OCR, UIA, clicks, input.
- Real browser control with existing login state: TMWebDriver, Chrome extension CDP bridge, DOM/JS/CDP actions.
- Dynamic composition of local Python capabilities instead of a predeclared GUI tool set.
- Reliable verification after every side effect.

Do not use this skill to copy GenericAgent's full agent loop, LLM client, or memory system. Hermes already owns those layers.

## Core Mechanism

GenericAgent's important mechanism is:

```text
observe -> generate minimal code_run Python -> execute -> return JSON evidence -> verify -> next action
```

A `code_run` block should dynamically import only the needed local modules:

```python
import json
# optional imports as needed:
# import win32gui, win32api, win32con
# from PIL import ImageGrab
# import pyperclip, uiautomation
# from TMWebDriver import TMWebDriver

result = {"ok": False, "action": "", "evidence": {}, "error": None}
# perform one minimal action or one observation
print(json.dumps(result, ensure_ascii=False, indent=2))
```

In Hermes, emulate this pattern with `execute_code` or `terminal` running a small Python script. Always return JSON.

## Desktop Control Recipe

1. Observe: enumerate windows with `win32gui.EnumWindows`, capture screenshots with `PIL.ImageGrab.grab`, inspect UIA/OCR only as needed.
2. Select target: verify title, hwnd, class, process, and rectangle before any side effect.
3. Act: use the minimum possible Win32/UIA/clipboard/mouse/keyboard action.
4. Verify: screenshot/OCR/UIA/window state after the action.
5. Report only verified results.

Useful references:

- `references/environment.md` for portable dependency configuration
- `references/code-run-core.md`
- `references/windows-control.md`
- `references/safety-rules.md`
- `references/session-lessons.md` for migration/spec pitfalls discovered while packaging this skill
- `templates/code-run-snippet.py`

## Browser Control Recipe

Use this priority order:

```text
DOM/Runtime.evaluate -> CDP Input.dispatchMouseEvent -> physical mouse click
```

For real login state, use an existing browser session or CloakBrowser persistent context. Verify with URL, title, DOM text, screenshot, or API response.

Useful references:

- `references/browser-control.md`
- `scripts/browser_cdp_probe.py`

## Safety Rules

Never use this skill to:

- Delete files or directories.
- Run `rm -rf`, `Remove-Item -Recurse -Force`, or equivalent destructive commands.
- Kill broad process classes such as all `python.exe` processes.
- Read or output credentials, API keys, cookies, or secrets.
- Submit payments or sensitive personal data without explicit confirmation.
- Click guessed coordinates without observation evidence.
- Claim success without verification.

Always:

- Confirm the target window before side effects.
- Keep each code_run snippet small.
- Return JSON with evidence.
- Verify after every side effect.
- Report failures honestly.

## Environment Configuration

This skill is portable. It must not hardcode a local GenericAgent checkout path.

Optional PowerShell setup when you want to reuse a specific GenericAgent checkout or Python environment:

```powershell
$env:GENERIC_AGENT_ROOT='D:\path\to\GenericAgent'
$env:GENERIC_AGENT_PYTHON='D:\path\to\GenericAgent\.venv\Scripts\python.exe'
```

`GENERIC_AGENT_PYTHON` is useful for helpers that need compiled packages such as Pillow/pywin32. If neither variable is set, helpers try the current Python and return truthful JSON setup hints when dependencies are unavailable.

See `references/environment.md`.

## Quick Local Probes

Run from this skill directory:

```powershell
python .\scripts\desktop_probe.py
python .\scripts\window_ops.py --list
python .\scripts\screenshot_ocr.py --screen
python .\scripts\browser_cdp_probe.py --status
```

## Verification Checklist

- [ ] `SKILL.md` frontmatter parses.
- [ ] Linked references/templates/scripts are present.
- [ ] Helper scripts compile.
- [ ] `desktop_probe.py` returns JSON.
- [ ] `window_ops.py --list` returns JSON.
- [ ] `screenshot_ocr.py --screen` either captures an image or returns a truthful JSON error.
- [ ] `browser_cdp_probe.py --status` returns connected/unavailable as JSON without crashing.
