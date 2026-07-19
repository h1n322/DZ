import json

import requests

OPENROUTER_URL ="https://openrouter.ai/api/v1/chat/completions"


def ask_openrouter(api,key,messages,model,temperature):
    response = requests.post(
        OPENROUTER_URL,
        header={
            "Athorization": f"Bearer {key}",
            "Content-Type":"application/json"
        },
        json={
            "model": model,
            messages: messages,
            "temperature": temperature
        },
        timeout= 120
    )

    response.raise_for_status()

    data = response.json()
    return data["choices"][0]["message"]["content"]