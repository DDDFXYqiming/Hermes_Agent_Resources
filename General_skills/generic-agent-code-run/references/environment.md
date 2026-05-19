# Environment Configuration

This skill is reusable and must not assume a machine-specific GenericAgent path.

## Optional Environment Variables

Configure these only when you want the helper scripts to reuse an existing GenericAgent checkout or a Python environment that already has Windows desktop/browser dependencies installed.

| Variable | Purpose |
|---|---|
| `GENERIC_AGENT_ROOT` | Path to a GenericAgent checkout/root directory. Helper scripts use it to locate modules such as `TMWebDriver.py`, `memory/ocr_utils.py`, and an optional `.venv`/`venv`. |
| `GENERIC_AGENT_PYTHON` | Explicit Python executable for helpers that need compiled dependencies such as Pillow/pywin32. Takes priority over auto-detecting `.venv` under `GENERIC_AGENT_ROOT`. |
| `HERMES_HOME` | Optional output base for screenshots. If unset, helpers use the current user's `.hermes` directory. |

## PowerShell Example

```powershell
$env:GENERIC_AGENT_ROOT='D:\path\to\GenericAgent'
$env:GENERIC_AGENT_PYTHON='D:\path\to\GenericAgent\.venv\Scripts\python.exe'
python .\scripts\desktop_probe.py
python .\scripts\screenshot_ocr.py --screen
```

## Behavior When Unconfigured

- Helpers first try the current Python environment.
- GenericAgent-specific imports are skipped unless a root can be discovered from the current working directory or `GENERIC_AGENT_ROOT`.
- If a compiled dependency such as Pillow is missing, `screenshot_ocr.py` returns a JSON error with a configuration hint instead of silently relying on a hardcoded local path.

## Packaging Rule

Do not write machine-specific local paths into this skill. Use placeholders in documentation and environment variables in scripts.
