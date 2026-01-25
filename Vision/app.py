from ollama import chat
from pathlib import Path

img = Path('architecture.png').read_bytes()

response = chat(
  model='gemma3',
  messages=[
    {
      'role': 'user',
      'content': 'What is in this image? Be concise.',
      'images': [img],
    }
  ],
)

print(response.message.content)