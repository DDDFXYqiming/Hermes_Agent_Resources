# Code_Run Core

GenericAgent's core is not a large static GUI toolset. Its core is `code_run`: a universal execution mechanism where the model writes short Python code, executes it locally, receives structured evidence, and decides the next action.

## Source Files

The exact GenericAgent checkout/root directory is machine-specific. Configure `GENERIC_AGENT_ROOT`, then treat these as root-relative references:

- `%GENERIC_AGENT_ROOT%\ga.py`
- `%GENERIC_AGENT_ROOT%\assets\tools_schema_cn.json`
- `%GENERIC_AGENT_ROOT%\assets\code_run_header.py`

See `references/environment.md` for portable setup.

## Pattern

```text
LLM -> code_run(Python) -> local capability library -> JSON evidence -> LLM
```

## Pseudocode

```python
def generic_agent_style_task(task):
    observation = observe()
    while not done(task, observation):
        code = make_minimal_python(task, observation)
        result = code_run(code)
        observation = verify(result)
```

## Hermes Translation

Hermes already has its own agent loop. Do not port GA's loop. Instead, when this skill is loaded, emulate `code_run` by using `execute_code` or `terminal` with short Python snippets that:

- import only the required modules;
- perform one observation or one small action;
- print JSON with `ensure_ascii=False`;
- include evidence: screenshot path, OCR text, hwnd/title, DOM text, URL, or explicit error.

## Standard Result Shape

```json
{
  "ok": true,
  "action": "observe_windows",
  "target": "optional target name",
  "evidence": {},
  "error": null
}
```
