# langchain-deepseek-extension

## Introduction
    This project supports the calculation of token counts.

    ref: https://api-docs.deepseek.com/zh-cn/quick_start/token_usage

## Examples

```python
from langchain_deepseek_extension.extension import ChatDeepSeekPlus

model = ChatDeepSeekPlus(model="deepseek-chat")

messages = [
    SystemMessage(content="you're a good assistant"),
    HumanMessage(content="hi! I'm bob"),
    AIMessage(content="hi!")
]
num = model.get_num_tokens_from_messages(messages)

```