from typing import List, Optional, Any, Sequence, Union, Dict, Type, Callable
import transformers
from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import BaseMessage
from langchain_core.tools import BaseTool


class ChatDeepSeekPlus(ChatDeepSeek):
    __tokenizer__ = transformers.AutoTokenizer.from_pretrained(
        "./", trust_remote_code=True
    )

    def get_num_tokens_from_messages(
        self,
        messages: List[BaseMessage],
        tools: Optional[
            Sequence[Union[Dict[str, Any], Type, Callable, BaseTool]]
        ] = None,
    ) -> int:
        num_tokens = 0
        for msg in messages:
            num_tokens += len(self.__tokenizer__.encode(msg.content))
        return num_tokens
