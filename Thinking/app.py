import requests
import json

# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/chat"

payload = {
    "model": "deepseek-r1",
    "messages": [{"role": "user", "content": "What is 17 * 23?"}],
    "stream": True,
    "options": {
        "num_predict": -1
    }
}

response = requests.post(OLLAMA_URL, json=payload, stream=True)

in_thinking = False

if response.status_code == 200:
    for line in response.iter_lines():
        if line:
            chunk = json.loads(line)
            
            if 'message' in chunk:
                message = chunk['message']
                
                if 'thinking' in message and message['thinking']:
                    if not in_thinking:
                        in_thinking = True
                        print('Thinking:\n', end='')
                    print(message['thinking'], end='')
                
                elif 'content' in message and message['content']:
                    if in_thinking:
                        print('\n\n' + '='*60)
                        print('Answer:')
                        print('='*60 + '\n')
                        in_thinking = False
                    print(message['content'], end='')
else:
    print(f"Error: {response.status_code}")