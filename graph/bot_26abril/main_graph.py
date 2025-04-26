from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.checkpoint.memory import MemorySaver
from .nodes import call_model

workflow = StateGraph(MessagesState)

# Edges
workflow.add_node("chatbot", call_model)
workflow.add_edge(START, "chatbot")
workflow.add_edge("chatbot", END)

memory = MemorySaver()

graph = workflow.compile(checkpointer=memory)
