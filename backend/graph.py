import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from state import DebuggerState
from tools import (
    detect_language,
    detect_errors,
    explain_code,
    suggest_fix
)

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

tools = [
    detect_language,
    detect_errors,
    explain_code,
    suggest_fix
]


def llm_node(state: DebuggerState):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}



def should_continue(state: DebuggerState):
    last_message = state["messages"][-1]

    if last_message.tool_calls:
        return "tools"

    return "__end__"


graph = StateGraph(DebuggerState)

graph.add_node("llm", llm_node)
graph.add_node("tools", ToolNode(tools))

graph.set_entry_point("llm")

graph.add_conditional_edges(
    "llm",
    should_continue
)

graph.add_edge("tools", "llm")

app = graph.compile()
