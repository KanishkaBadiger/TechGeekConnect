import requests
import json

# def get_ai_response(user_input):
def get_ai_response(prompt):
    url = "http://localhost:11434/api/generate"
    # prompt = f"Answer in 10-15 lines: \n{user_input}"

    payload = {
        "model": "phi",
        "prompt": prompt,
        "stream": False,
        "options":{
            "num_predict":120,
            "temperature":0.8
        }
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json()["response"]
    else:
        return "Error connecting to Ollama"

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "phi"

def generate_response(prompt):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code != 200:
        return "Ollama server not responding."

    data = response.json()
    return data.get("response", "No response generated.")



def ask_ollama(prompt, model="phi"):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code != 200:
        return "Ollama server not responding."

    data = response.json()
    return data.get("response", "No response generated.")



