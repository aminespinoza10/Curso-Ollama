import requests
import json
import time

# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

def non_streaming_example():
    """Ejemplo sin streaming - Debes esperar la respuesta completa"""
    print("\n" + "="*60)
    print("MODO SIN STREAMING")
    print("="*60)
    print("Esperando la respuesta completa...\n")
    
    start_time = time.time()
    
    payload = {
        "model": "llama3.2",
        "prompt": "Escribe un poema corto sobre inteligencia artificial",
        "stream": False
    }
    
    response = requests.post(OLLAMA_URL, json=payload)
    
    end_time = time.time()
    
    if response.status_code == 200:
        data = response.json()
        print("Respuesta:")
        print(data['response'])
        print(f"\n⏱️  Tiempo total: {end_time - start_time:.2f} segundos")
        print(f"📊 Tokens generados: {data.get('eval_count', 'N/A')}")
        print(f"⚡ Velocidad de generación: {data.get('eval_count', 0) / (data.get('eval_duration', 1) / 1e9):.2f} tokens/seg")
    else:
        print(f"Error: {response.status_code}")

def streaming_example():
    """Ejemplo con streaming - muestra la respuesta mientras se genera"""
    print("\n" + "="*60)
    print("MODO CON STREAMING")
    print("="*60)
    print("Respuesta (streaming):\n")
    
    start_time = time.time()
    first_token_time = None
    token_count = 0
    
    payload = {
        "model": "llama3.2",
        "prompt": "Escribe un poema corto sobre inteligencia artificial",
        "stream": True
    }
    
    response = requests.post(OLLAMA_URL, json=payload, stream=True)
    
    if response.status_code == 200:
        for line in response.iter_lines():
            if line:
                chunk = json.loads(line)
                
                if 'response' in chunk:
                    print(chunk['response'], end='', flush=True)
                    
                    if first_token_time is None:
                        first_token_time = time.time()
                
                if chunk.get('done', False):
                    end_time = time.time()
                    print("\n")
                    print(f"\n⏱️  Tiempo total: {end_time - start_time:.2f} segundos")
                    print(f"⚡ Tiempo al primer token: {first_token_time - start_time:.2f} segundos")
                    print(f"📊 Tokens generados: {chunk.get('eval_count', 'N/A')}")
                    print(f"⚡ Velocidad de generación: {chunk.get('eval_count', 0) / (chunk.get('eval_duration', 1) / 1e9):.2f} tokens/seg")
    else:
        print(f"Error: {response.status_code}")

def main():
    print("COMPARACIÓN DE RENDIMIENTO ENTRE STREAMING Y NO STREAMING")
    print("=" * 60)
    
    # Ejecutar primero sin streaming
    non_streaming_example()
    
    # Esperar un momento entre ejemplos
    time.sleep(2)
    
    # Ejecutar con streaming
    streaming_example()
    
    print("\n" + "="*60)
    print("¿NOTASTE LA DIFERENCIA?")
    print("="*60)

if __name__ == "__main__":
    main()
