# Few Shot Prompting
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Few Shot Prompting: Directly giving the inst to the model and few example to the model before response to the user
SYSTEM_PROMPT = """
You should only ans the coding related questions. Do not ans anything else. If user ask something else other then coding, just say sorry

Rule:
- Strictly follow the output in JSON formate

Output Formate:
{{
  "code": "string" or null,
  "isCodingQuestion": boolean
}}

Examples:
Q: Can you explain the a + b whole square?
A: {{"code": null, "isCodingQuestion": false}}

Q: Hey, Write a code in python for adding two numbers.
A: {{"code": "def add(a,b):
                  return a +b", "isCodingQuestion": true}}
"""

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
  model="gemini-3.8-flash",
  messages=[
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "Write a code in python for adding two numbers"}
  ]
)

print(response.choices[0].message.content)