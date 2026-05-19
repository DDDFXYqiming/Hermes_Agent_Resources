# Safety Rules

`code_run` is powerful. Treat it as a sharp local execution path.

## Forbidden

- Delete files or directories.
- Run recursive destructive deletion commands.
- Kill broad process classes such as all `python.exe`.
- Read or print secrets, API keys, cookies, passwords, auth files, or `.env` contents.
- Submit payments or sensitive personal data without explicit user confirmation.
- Click guessed coordinates.
- Operate an unverified window.
- Pretend an action succeeded without evidence.

## Required

- One snippet = one observation or one small side effect.
- Print JSON with `ensure_ascii=False`.
- Verify target window before GUI side effects.
- Verify after every side effect.
- Keep screenshots in a temp/cache path, not in project root.
- Report errors exactly.

## High-Risk Stop Points

Stop and ask the user when the next action would submit payment, delete data, expose credentials, send private messages to third parties, or make irreversible account changes.
