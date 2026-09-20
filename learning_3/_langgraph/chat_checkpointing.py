from dotenv import load_dotenv
from typing import TypedDict
from typing_extensions import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.mongodb import MongoDBSaver

load_dotenv()

llm = init_chat_model(
  model="gemini-3.1-flash-lite",
  model_provider="google_genai",
  temperature=0.7,
)

class State(TypedDict):
  messages: Annotated[list, add_messages]

def chatbot(state: State):
  response = llm.invoke(state.get("messages"))
  return {"messages": [response]}

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

def compile_graph_with_checkpoint(checkpoint):
  return graph_builder.compile(checkpointer=checkpoint)

MONGODB_URI = "mongodb://root:root@localhost:27017"

with MongoDBSaver.from_conn_string(MONGODB_URI) as checkpoint:
  graph_with_checkpointer = compile_graph_with_checkpoint(checkpoint=checkpoint)

  config = {
    "configurable": {
      "thread_id": "1"
    }
  }

  for chunk in graph_with_checkpointer.stream(
    State({"messages": ["What i am learning?"]}),
    config,
    stream_mode="values"
  ):
    chunk["messages"][-1].pretty_print()