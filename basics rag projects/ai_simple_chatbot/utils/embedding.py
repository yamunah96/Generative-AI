import numpy as np
import requests
import  os
from dotenv import load_dotenv  
load_dotenv()  # Load environment variables from .env file

api_key= os.getenv('my_api_key')
print(api_key)

def get_embedding(text, model="text-embedding-3-small"):
    url='https://api.euron.one/api/v1/euri/embeddings'
    headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
    }
    payload = {
    "model": model,
    "input": text,
    }
    response = requests.post(url, json=payload, headers=headers)
    # print(response.json())
    return np.array(response.json()['data'][0]['embedding'])

print(get_embedding("whats deep learning"))