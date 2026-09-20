from ollama import chat
import requests
from bs4 import BeautifulSoup

url = "https://developer.mozilla.org/en-US"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")

webpage_text = " ".join([
  p.getText() for p in soup.find_all(["h1", "h2", "h3"])
])[:5000]

# 2. Pass the extracted text to Ollama
system_prompt = """
You are a helpful summarizer. Extract key information from the provided text concisely.
Respond in a clear and concise manner.
"""

messages = [
    {"role": "system", "content": system_prompt},
    {
      "role": "user",
      "content": f"Summarize the main purpose of this website based on the text below:\n\n{webpage_text}",
    },
]

response = chat(model="gemma3:270m", messages=messages, stream=True)

for chunk in response:
  print(chunk["message"]["content"], end="", flush=True)

