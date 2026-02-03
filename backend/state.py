from typing import TypedDict, List
from langchain_core.messages import BaseMessage


class DebuggerState(TypedDict):
    messages: List[BaseMessage]
    code: str
    language: str
