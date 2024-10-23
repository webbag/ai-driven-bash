#!/usr/bin/env python3
import os
import requests
import json
import sys
import re

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
API_URL = "https://api.openai.com/v1/chat/completions"

if not OPENAI_API_KEY:
    print("Brak klucza API. Ustaw zmienną środowiskową OPENAI_API_KEY.")
    sys.exit(1)

argument = ' '.join(sys.argv[1:])

if len(sys.argv) > 1:
    argument = ' '.join(sys.argv[1:])
else:
    print("Podaj proszę pytanie")

REQUEST_DATA = {
    "model": "gpt-4o",
    "messages": [
        {
            "role": "system",
            "content": (
                "Jesteś ekspertem od systemu Linux Debian i służysz zawsze gotowym rozwiązaniem. "
                "Proszę zwróć mi tekst w formacie sformatowanym do wyświetlenia w terminalu bez widocznych znaków formatowania Markdown, takich jak backticki (`), gwiazdki (**), oraz bloki kodu otoczone trzema backtickami. Zamiast tego: \n"               
                "Pogrubione fragmenty (**tekst**) powinny być zwrócone jako tekst sformatowany na pogrubiony.\n"
                "Tekst w backtickach (`tekst`) powinien zostać bez zmian.\n"
                "Bloki kodu otoczone trzema backtickami (```bash) mają być wyświetlone bez backticków oraz nazwy języka, a kod w środku powinien być sformatowany.\n"
                "Nie chcę widzieć żadnych znaków Markdown w wynikowej treści, ale chcę zachować formatowanie."
            )
        },
        {
            "role": "user",
            "content": argument
        }
    ],
    "temperature": 0.3,
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

    # Pobieranie odpowiedzi
    content = response.json().get('choices', [{}])[0].get('message', {}).get('content', "Brak treści w odpowiedzi.")

    # Wyświetlanie sformatowanego tekstu
    print(content)
else:
    print(f"Błąd w żądaniu: {response.status_code} - {response.text}")
