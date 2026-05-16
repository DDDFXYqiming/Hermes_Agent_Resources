# Browser Control

GenericAgent controls real browsers with TMWebDriver and a Chrome Extension/CDP bridge. Use this only when Hermes' normal browser tools are insufficient or when a real logged-in browser profile is required.

## Source Files

The exact GenericAgent location is environment-specific. Configure `GENERIC_AGENT_ROOT` first, then refer to files relative to that root:

- `%GENERIC_AGENT_ROOT%\TMWebDriver.py`
- `%GENERIC_AGENT_ROOT%\simphtml.py`
- `%GENERIC_AGENT_ROOT%\memory\tmwebdriver_sop.md`
- `%GENERIC_AGENT_ROOT%\assets\tmwd_cdp_bridge\`

See `references/environment.md` for portable setup.

## Priority Order

```text
DOM / JS Runtime.evaluate
> CDP Input.dispatchMouseEvent
> physical mouse click
```

## Evidence

Every browser action must verify at least one of:

- current URL;
- document title;
- DOM text;
- screenshot;
- API response;
- visible state after interaction.

## Pseudocode

```python
import json
from TMWebDriver import TMWebDriver

driver = TMWebDriver()
page = driver.current_page()
print(json.dumps({
    "ok": True,
    "action": "browser_observe",
    "url": page.evaluate("location.href"),
    "title": page.evaluate("document.title"),
    "text_preview": page.evaluate("document.body.innerText.slice(0, 2000)"),
}, ensure_ascii=False))
```

If TMWebDriver is unavailable, return JSON saying unavailable instead of crashing.
