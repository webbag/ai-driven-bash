#!/usr/bin/env python3
import os
import requests
import json
import sys

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
API_URL = "http://localhost:11434/v1/chat/completions"

if not OPENAI_API_KEY:
    print("Brak klucza API. Ustaw zmienną środowiskową OPENAI_API_KEY.")
    sys.exit(1)

argument = ' '.join(sys.argv[1:])

if len(sys.argv) > 1:
    argument = ' '.join(sys.argv[1:])
else:
    print("Podaj proszę pytanie")

REQUEST_DATA = {
    "model": "mistral:latest",
    "messages": [
        {
            "role": "system",
            "content": (
                "Jesteś ekspertem od systemu Linux Debian i służysz zawsze gotowym rozwiązaniem. "
                "Będę zadawać Ci pytania w różnych formach. Twoja odpowiedź będzie zależna od formy mojego pytania. "
                "\n\nPrzykłady:\n"
                "Jeśli użyję jednego wyrazu, potraktuj to jako polecenie bash. Zachowuj się jak Linux Manual i podaj 5 zaawansowanych przykładów użycia polecenia.\n"
                "Jeśli otrzymasz więcej niż jedno słowo, potraktuj to jako pytanie i udziel odpowiedzi jako mój partner do konfiguracji i administracji systemu Linux.\n"
            )
        },
        {
            "role": "user",
            "content": argument
        }
    ],
    "temperature": 1,
    "max_tokens": 256,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0
}

response = requests.post(
    API_URL,
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    },
    data=json.dumps(REQUEST_DATA)
)

if response.status_code == 200:
    content = response.json().get('choices', [{}])[0].get('message', {}).get('content', "Brak treści w odpowiedzi.")
    print(content)
else:
    print(f"Błąd w żądaniu: {response.status_code} - {response.text}")
