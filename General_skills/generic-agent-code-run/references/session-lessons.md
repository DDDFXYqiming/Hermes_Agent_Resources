# Session Lessons

Use these notes when extending or reusing `generic-agent-code-run`.

## Keep the spec centered on Code_Run

The GenericAgent migration should not be described as a broad collection of GUI helper scripts. The durable core is:

```text
minimal fixed tools + code_run universal execution + local capability libraries + observe/act/verify
```

When writing specs or implementation notes for this skill, lead with `code_run`, then explain desktop/browser helpers as examples of what code_run can dynamically invoke.

## Keep review specs concise

For user review, avoid long phase-by-phase prose unless asked. Prefer a final, concrete spec with:

- source directory;
- target directory;
- exact files to create;
- pseudocode commands;
- validation commands;
- acceptance criteria.

## Platform frontmatter pitfall

If a locally installed Skill unexpectedly reports `unsupported platform` on Windows native Hermes, inspect the `platforms` frontmatter. In environments where YAML parsing falls back to simple key/value parsing, inline YAML like `platforms: [windows]` can be treated as a string and fail platform matching. For local/private skills, omit `platforms` unless restriction is necessary, or use a parser-verified format.

## Binary dependency handling

Do not blindly add another project venv's `site-packages` to Hermes Python for compiled packages such as Pillow. If a helper needs compiled dependencies from GenericAgent, re-exec that helper through a configurable environment, not a hardcoded local path:

```powershell
$env:GENERIC_AGENT_ROOT='D:\path\to\GenericAgent'
$env:GENERIC_AGENT_PYTHON='D:\path\to\GenericAgent\.venv\Scripts\python.exe'
python .\scripts\screenshot_ocr.py --screen
```

`GENERIC_AGENT_PYTHON` takes priority when set. Otherwise helpers may discover `.venv`/`venv` under `GENERIC_AGENT_ROOT`. If neither is configured and the current Python lacks a compiled dependency, return JSON evidence with a clear setup hint instead of pretending success.
