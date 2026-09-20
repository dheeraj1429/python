# Zero Shot Prompting
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Zero Shot Prompting: Directly giving the inst to the model

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
  model="gemini-3.8-flash",
  messages=[
    {"role": "system", "content": "You are an expert in Maths and only ans the maths related questions"},
    {"role": "user", "content": "Can you please provide the basic example of python code?"}
  ]
)

print(response.choices[0].message.content)