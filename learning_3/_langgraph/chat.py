from dotenv import load_dotenv
from typing import TypedDict
from typing_extensions import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model

load_dotenv()

llm = init_chat_model(
  model="gemini-3.1-flash-lite",
  model_provider="google_genai",
  temperature=0.7,
)

class State(TypedDict):
  messages: Annotated[list, add_messages]

def chatbot(state: State):
  print(f"\n\n\nInside the chatbot node with state: {state}")
  response = llm.invoke(state.get("messages"))
  return {"messages": [response]}

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

updated_state = graph.invoke(State({"messages": ["Hey what is my name"]}))
print(f"\n\n\nupdated_state: {updated_state}")