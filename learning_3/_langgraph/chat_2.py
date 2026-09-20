import os
from dotenv import load_dotenv
from typing import TypedDict, Optional, Literal
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from openai import OpenAI

load_dotenv()

client = OpenAI(
  api_key=os.getenv("GEMINI_API_KEY"),
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

class State(TypedDict):
  user_query: str
  llm_output: Optional[str]
  is_good: bool

def chatbot(state: State):
  print(f"\n\n\nCalled chatbot node {state}")
  response = client.chat.completions.create(
    model="gemini-3.1-flash-lite",
    messages=[
      { "role": "user", "content": state.get("user_query") }
    ]
  )

  state["llm_output"] = response.choices[0].message.content
  return state

def chatbot_2(state: State):
  print(f"\n\n\nCalled chatbot_2 node {state}")
  response = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[
      { "role": "user", "content": state.get("user_query") }
    ]
  )

  state["llm_output"] = response.choices[0].message.content
  return state

def end_node(state: State):
  print(f"\n\n\nCalled end_node {state}")
  return state

def evaluation_response(state: State) -> Literal["chatbot_2", "end_node"]:
  print(f"\n\n\nevaluation_response state; {state}")
  if state.is_good:
    return "end_node"

  return "chatbot_2"

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("chatbot_2", chatbot_2)
graph_builder.add_node("end_node", end_node)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", evaluation_response)

graph_builder.add_edge("chatbot_2", "end_node")
graph_builder.add_edge("end_node", END)

graph = graph_builder.compile()

updated_sate = graph.invoke(State({"user_query": "Hey, what is 2 + 2?"}))
print(f"updated_state: {updated_sate}")