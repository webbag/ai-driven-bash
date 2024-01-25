#!/bin/bash

OPENAI_API_KEY=""
API_URL="https://api.openai.com/v1/chat/completions"
argument="$1"
REQUEST_DATA="{
  \"model\": \"gpt-3.5-turbo\",
  \"messages\": [
    {
      \"role\": \"system\",
      \"content\": \"Będzie udzielać krótkich wyjaśnień dotyczących bash w linux. Podam Tobie nazwę komendy a Ty podasz mi 5 przykładów użycia z wyjaśnieniem nie dłuższym niż 5 wyrazów.\nKażdy z przykładów w osobnym punkcie. Użyj formatowania w bash oraz kolorów. \n\"
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