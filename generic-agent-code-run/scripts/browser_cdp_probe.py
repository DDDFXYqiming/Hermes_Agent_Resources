#!/usr/bin/env python3
import argparse
import json
import sys
import traceback
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from ga_env import add_generic_agent_paths, env_status  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description="Probe GenericAgent TMWebDriver/CDP availability")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--current-page", action="store_true")
    args = ap.parse_args()

    ga_root, added_paths = add_generic_agent_paths()
    try:
        import TMWebDriver  # noqa: F401
        payload = {
            "ok": True,
            "action": "browser_cdp_probe",
            "status": "module_available",
            "environment": env_status(ga_root),
            "added_paths": added_paths,
            "note": "TMWebDriver import succeeded. Current-page probing is intentionally non-invasive in this helper.",
        }
    except Exception as e:
        payload = {
            "ok": False,
            "action": "browser_cdp_probe",
            "status": "unavailable",
            "environment": env_status(ga_root),
            "added_paths": added_paths,
            "error": {"type": type(e).__name__, "message": str(e), "traceback": traceback.format_exc()},
            "hint": "Set GENERIC_AGENT_ROOT to a GenericAgent checkout/root directory if TMWebDriver should be available.",
        }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
