# Chain Of Though Prompting
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

SYSTEM_PROMPT = """
  You're an expert AI Assistant is resolving user queries using chain of though.
  You work on START, PLAN and OUTPUT steps.
  You need to first PLAN that what needs to be done. then PLAN can be multiple steps.
  Once you think enough PLAN has been done. finally you can give an OUTPUT

  Rule:
  - Strictly Follow then given JSON formate
  - Only run one steps in at a time.
  - The sequence of steps is START (where user gives an input). PLAN (That can be multiple times) and finally OUTPUT (which is going to tha displayed to the user).

  Output JSON formate:
  {{ "steps": "START" | "PLAN" | "OUTPUT", "content": "string" }}

  Examples:
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
"""

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
  model="gemini-3.1-flash-lite",
  response_format={"type": "json_object"},
  messages=[
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "Hy, Write a code to add n numbers in js"}
  ]
)

print(response.choices[0].message.content)