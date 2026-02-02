import requests

OLLAMA_URL = "http://localhost:11434/api/chat"

def ask_llm(message: str, model_name : str, temperature : float, max_tokens : int) -> str:
    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": "You are a nice AI assistant"},
            {"role": "user", "content": message}
        ],
        "stream": False,
        "options": {
            "temperature": temperature,
            "num_predict": max_tokens
        }
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=60)
    response.raise_for_status()

    data = response.json()
    return data["message"]["content"]