import json
import traceback


def main():
    result = {
        "ok": False,
        "action": "",
        "target": None,
        "evidence": {},
        "error": None,
    }
    try:
        # Write one minimal observation or action here.
        # Import only the modules needed for that action.
        result["ok"] = True
        result["action"] = "describe_action_here"
        result["evidence"] = {}
    except Exception as e:
        result["ok"] = False
        result["error"] = {
            "type": type(e).__name__,
            "message": str(e),
            "traceback": traceback.format_exc(),
        }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
