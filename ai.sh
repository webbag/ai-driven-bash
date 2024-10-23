#!/bin/bash


OPENAI_API_KEY=""
API_URL="http://localhost:11434/v1/chat/completions"
argument="$@"
REQUEST_DATA="{
  \"model\": \"mistral:latest\",
  \"messages\": [
    {
      \"role\": \"system\",
      \"content\": \"Jesteś ekspertem od systemu Linux Debian i służysz zawsze gotowym rozwiązaniem. Będę zadawać Ci pytania w różnych formach. Twoja odpowiedź będzie zależna od formy mojego pytania. \n\nPrzykłady:\nJeśli użyję jednego wyrazu, potraktuj to jako polecenie bash. Zachowuj się jak Linux Manual i podaj 5 zaawansowanych przykładów użycia polecenia.\nJeśli otrzymasz więcej niż jedno słowo, potraktuj to jako pytanie i udziel odpowiedzi jako mój partner do konfiguracji i administracji systemu Linux.\n\"
    },
    {
      \"role\": \"user\",
      \"content\": \"${argument}\"
    }
  ],
  \"temperature\": 1,
  \"max_tokens\": 256,
  \"top_p\": 1,
  \"frequency_penalty\": 0,
  \"presence_penalty\": 0
}"

response=$(curl -s -H "Content-Type: application/json" -H "Authorization: Bearer $OPENAI_API_KEY" -d "$REQUEST_DATA" "$API_URL")
content=$(echo "$response" | jq -r '.choices[0].message.content')
echo "$content"