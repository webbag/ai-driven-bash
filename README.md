# AI Driven Bash Documentation

This bash script is designed to interact with the OpenAI GPT-3.5 API to provide examples of bash command usage based on a provided command name. It generates short explanations for the provided bash commands.

## Usage

Ensure you have set up your OpenAI API key in the `OPENAI_API_KEY` variable within the script.

```bash
./ai.sh [command_name]
```

Replace `[command_name]` with the bash command you want to explore.

## Overview

The script utilizes the OpenAI GPT-3.5 model to generate examples of command usage in bash for Linux systems. It prompts the user to provide a command name and generates five examples with brief explanations, each within five words, using bash formatting and colors.

## Script Details

- **OPENAI_API_KEY**: Your OpenAI API key should be added to this variable. Obtain your API key from the OpenAI platform.

- **API_URL**: The endpoint URL for the OpenAI GPT-3.5 API.

- **REQUEST_DATA**: JSON structure containing model configuration, user input, and generation parameters for the API request.

- **response**: Captures the response from the API request.

- **content**: Extracts the generated examples from the API response using `jq`.

## Example

```bash
./ai.sh netstat

1. netstat -a
   Wyświetla wszystkie porty wraz z adresami IP na których serwer nasłuchuje.

2. netstat -t
   Wyświetla wszystkie połączenia TCP.

3. netstat -u
   Wyświetla wszystkie połączenia UDP.

4. netstat -n
   Wyświetla adresy IP w formacie liczbowym.

5. netstat -p
   Wyświetla informacje o procesach powiązanych z danymi połączeniami.




```

This command will prompt the script to generate five examples of `netstat` command usage with brief explanations.

## Requirements

- Bash environment
- OpenAI GPT-3.5 API access and key
- Curl
- jq (a lightweight and flexible command-line JSON processor)

## License

This script is released under the [MIT License](LICENSE). Feel free to modify and distribute it as per your requirements.
