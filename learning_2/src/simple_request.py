from ollama import chat

system_prompt = """
You are a helpful assistant that explains programming concepts clearly in python.
Please provide examples and explanations.
Respond in a clear and concise manner.
"""

messages = [
    {
        'role': 'system',
        'content': system_prompt,
    },
    {
        'role': 'user',
        'content': 'Explain list comprehensions in Python.',
    },
]

response = chat(
  model="gemma3:270m",
  messages=messages,
  stream=True
)

for chunk in response:
  print(chunk['message']['content'], end='', flush=True)

# from ollama import generate

# system prompt:
# system_prompt = """
# You are a helpful assistant that explains programming concepts clearly in python.
# Please provide examples and explanations.
# Respond in a clear and concise manner.
# """

# response = generate(
#     model="gemma3:270m",
#     prompt=f"{system_prompt}",
#     stream=True
# )

# for chunk in response:
#   print(chunk.response, end="", flush=True)