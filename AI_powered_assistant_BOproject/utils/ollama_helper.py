import requests
import json

def get_ai_response(user_input):
    url = "http://localhost:11434/api/generate"
    prompt = f"Answer in 10-15 lines: \n{user_input}"

    payload = {
        "model": "phi",
        "prompt": prompt,
        "stream": False,
        "options":{
            "num_predict":80,
            "temperature":0.3
        }
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json()["response"]
    else:
        return "Error connecting to Ollama"

