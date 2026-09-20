import os
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional

load_dotenv()

client = OpenAI(
  api_key=os.getenv("GEMINI_API_KEY"),
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# client = OpenAI(
#   base_url="http://localhost:11434",
#   api_key="ollama"
# )

def send_user_email(email: str) -> str:
  print(f"Hey i am from python, I am sending the email {email}")
  return True

def run_command(cmd: str):
  result = os.system(cmd)
  return result

SYSTEM_PROMPT = """
  You're an expert AI Assistant is resolving user queries using chain of though.
  You work on START, PLAN and OUTPUT steps.
  You need to first PLAN that what needs to be done. then PLAN can be multiple steps.
  Once you think enough PLAN has been done. finally you can give an OUTPUT.
  You can also call a tool if required from the list of available tools.
  for every tool call wait for the observe step which is the output of the function called.

  Rule:
  - Strictly Follow then given JSON formate
  - Only run one steps in at a time.
  - The sequence of steps is START (where user gives an input). PLAN (That can be multiple times) and finally OUTPUT (which is going to tha displayed to the user).

  Output JSON formate:
  { "step": "START" | "PLAN" | "TOOL" | "OUTPUT", "content": "string" }

  Available Tools:
  - send_user_email(email: str): Takes user email as string to send the email to user.
  - run_command(cmd: str): Take cmd as string and return the result of that command.

  Examples 1:
  START: Hey, Can you solve 2 + 3 * 5 / 10
  PLAN: { "step": "PLAN", "content": "Seems like user is interested in maths problem" }
  PLAN: { "step": "PLAN", "content": "looking at the problem, we should solve this using BODMAS method" }
  PLAN: { "step": "PLAN", "content": "Yes, The BODMAS is corret thing to done here" }
  PLAN: { "step": "PLAN", "content": "first we must multiple 3 * 5 that is 15" }
  PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 15 / 10" }
  PLAN: { "step": "PLAN", "content": "We must perform divide that 15 / 10 = 1.5" }
  PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 1.5" }
  PLAN: { "step": "PLAN", "content": "Now finally perform that addition 2 + 1.5 = 3.5" }
  OUTPUT: { "step": "OUTPUT", "content": "3.5" }

  Examples 2:
  START: Hello can you send email my email is: dheerajsingh123@gmail.com
  PLAN: { "step": "PLAN", "content": "Lets see we have any tool available to send the email" }
  PLAN: { "step": "PLAN", "content": "looking at the problem, we should use the send_user_email function to send the email" }
  PLAN: { "step": "TOOL", "content": "Yes, The send_user_email is correct to send the email and we can call the send_user_email function with input dheerajsingh123@gmail.com" }
  PLAN: { "step": "TOOL", "tool": "send_user_email", "input": "dheerajsingh123@gmail.com" }
  PLAN: { "step": "OBSERVER", "content": "The send_user_email function called to send the user email", "input": "dheerajsingh123@gmail.com" }
  OUTPUT: { "step": "OUTPUT", "content": "Done, What i can do next" }
"""

available_tools = {
  "send_user_email": send_user_email
}

class MyOutputFormat(BaseModel):
  step: str = Field(..., description="This ID of the step. Example: PLAN, TOOL, OBSERVER and OUTPUT")
  content: Optional[str] = Field(None, description="The optional string content for the step")
  tool: Optional[str] =  Field(None, description="The ID of the tool to call")
  input: Optional[str] = Field(None, description="The input params for the tool")

def main():
  user_input = input("> ")
  message_history = []
  message_history.append({"role": "system", "content": SYSTEM_PROMPT})
  message_history.append({"role": "user", "content": user_input})
  while True:
    response = client.chat.completions.parse(
      model="gemini-3.1-flash-lite",
      messages=message_history, 
      response_format=MyOutputFormat)
    raw_result = response.choices[0].message.content
    print("raw_result:",raw_result)
    parse_result = response.choices[0].message.parsed
    print("parse_result:",parse_result)
    message_history.append({"role": "assistant", "content": raw_result})

    if(parse_result.step == "PLAN"):
      print("🧠", parse_result.content)
      continue

    if(parse_result.step == "TOOL"):
      print("🔨", parse_result.content)
      tool_input = parse_result.input
      if tool_input:
        print(f"🧰 parsed tool input {tool_input}")
        available_tools['send_user_email'](tool_input)
        print("Called tool completed")

    if(parse_result.step == "OBSERVER"):
      print("🔨", parse_result.content)
      continue

    if(parse_result.step == "OUTPUT"):
      print("🤖", parse_result.content)
      break

main()