# llm.py

import requests

from config import (
    OLLAMA_URL,
    MODEL
)

def clean_response(text):

    garbage = [
        "[Your Name]",
        "[Company Name]",
        "[Email]",
        "[Phone]",
        "placeholder"
    ]

    for item in garbage:
        text = text.replace(item, "")

    return text.strip()


def ask_llm(prompt):

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=1200
    )

    response.raise_for_status()

    data = response.json()

    cleaned = clean_response(
        data["response"]
    )

    return cleaned