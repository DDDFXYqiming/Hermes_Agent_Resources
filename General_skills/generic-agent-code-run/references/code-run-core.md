# Code_Run Core

<!-- zh-main-begin -->

## 中文主体说明：Hermes_Agent_Resources 参考资料：code run core

- 本文档是通用技能资料。中文部分说明用途、输入、输出、执行步骤、验证标准和注意事项；保留必要英文标识以保证工具可运行。
- 阅读顺序建议：先看本中文说明，确认任务类型和验收标准；再阅读下方原始细则、模板或命令；最后按当前任务补充必要上下文并执行。
- 公开共享要求：不要写入本机绝对路径、个人目录、账号标识、真实密钥、临时下载目录或过细来源索引。若需要引用本地材料，用抽象描述或环境变量占位。

### 中文使用要点

- 先确认用户目标、输入材料、输出格式和验收标准，再选择本文档中的对应流程。
- 所有脚本、命令、字段名、模型名、平台名、文件名和示例代码保持原样，避免破坏可执行性。
- 面向用户的解释、报告、检查清单、风险提示和交付说明应使用中文。
- 遇到英文原文与中文说明冲突时，以不破坏工具执行为前提，优先遵循中文说明中的安全边界和验收要求。
- 完成后必须运行相关验证：语法检查、文件存在性检查、导出结果检查、截图或日志核对、敏感信息扫描。

<!-- zh-main-end -->


GenericAgent's core is not a large static GUI toolset. Its core is `code_run`: a universal execution mechanism where the model writes short Python code, executes it locally, receives structured evidence, and decides the next action.

## Source Files

### 中文：Source Files

- 本节说明 `Source Files` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Source Files

The exact GenericAgent checkout/root directory is machine-specific. Configure `GENERIC_AGENT_ROOT`, then treat these as root-relative references:

- `%GENERIC_AGENT_ROOT%\ga.py`
- `%GENERIC_AGENT_ROOT%\assets\tools_schema_cn.json`
- `%GENERIC_AGENT_ROOT%\assets\code_run_header.py`

See `references/environment.md` for portable setup.

## Pattern

### 中文：Pattern

- 本节说明 `Pattern` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Pattern

```text
LLM -> code_run(Python) -> local capability library -> JSON evidence -> LLM
```

## Pseudocode

### 中文：Pseudocode

- 本节说明 `Pseudocode` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Pseudocode

```python
def generic_agent_style_task(task):
    observation = observe()
    while not done(task, observation):
        code = make_minimal_python(task, observation)
        result = code_run(code)
        observation = verify(result)
```

## Hermes Translation

### 中文：Hermes Translation

- 本节说明 `Hermes Translation` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Hermes Translation

Hermes already has its own agent loop. Do not port GA's loop. Instead, when this skill is loaded, emulate `code_run` by using `execute_code` or `terminal` with short Python snippets that:

- import only the required modules;
- perform one observation or one small action;
- print JSON with `ensure_ascii=False`;
- include evidence: screenshot path, OCR text, hwnd/title, DOM text, URL, or explicit error.

## Standard Result Shape

### 中文：Standard Result Shape

- 本节说明 `Standard Result Shape` 相关的任务目标、输入、输出、关键约束和验收标准。
- 优先用中文向用户解释本节做什么、怎么用、失败时怎么办；下方保留的英文细则、参数、代码和命令作为机器可读规范。
- 执行前先核对任务前置条件：所需文件、所需依赖、所需环境变量、所需权限是否齐备。
- 执行后必须验证：文件是否存在、命令是否成功、产物是否完整、是否引入敏感信息。
- 如果本节是参考性章节而不是操作步骤，重点是给读者一个中文索引和阅读顺序，而不是直接产生新文件。
### 中文：中文标题：Standard Result 形状

```json
{
  "ok": true,
  "action": "observe_windows",
  "target": "optional target name",
  "evidence": {},
  "error": null
}
```
