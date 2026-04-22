import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key= os.getenv('my_api_key')
def generate_completion(prompt,model="gpt-4.1-nano",temperature=0.3):
    url = "https://api.euron.one/api/v1/euri/chat/completions"
    headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [{"role":"user","content":prompt}],
        "max_tokens": 500,
        "temperature": temperature,
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        return f"API Error {response.status_code}: {response.text}"

    try:
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError) as e:
        return f"Failed to parse response: {e}\nRaw response: {response.text}"
