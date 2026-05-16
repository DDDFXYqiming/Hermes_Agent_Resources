# Source Map

This skill is a distilled migration of the GenericAgent operation pattern, not a source-code copy.

All paths below are relative to the configured `GENERIC_AGENT_ROOT`; see `references/environment.md`.

| GenericAgent file | Skill usage |
|---|---|
| `ga.py` | Understand tool registration and `code_run` orchestration |
| `agent_loop.py` | Reference only; do not port loop into Hermes |
| `llmcore.py` | Reference only; Hermes owns model routing |
| `assets/tools_schema_cn.json` | Shows mounted tools are minimal and `code_run` carries most capability |
| `assets/code_run_header.py` | Safety prefix inspiration |
| `memory/ljqCtrl.py` | Windows screenshot/click/window primitives |
| `memory/ocr_utils.py` | OCR and window screenshot routines |
| `memory/ui_detect.py` | UI element detection ideas |
| `TMWebDriver.py` | Browser/CDP bridge control |
| `simphtml.py` | DOM simplification ideas |
| `assets/tmwd_cdp_bridge/` | Chrome extension/CDP bridge reference |
| `memory/tmwebdriver_sop.md` | Browser SOP reference |
| `memory/cloakbrowser_sop.md` | CloakBrowser real-profile SOP reference |
