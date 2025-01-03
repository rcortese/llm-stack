import requests
import sys

base_url = 'http://ollama:11434'
url = f'{base_url}/api/pull'
headers = {'Content-Type': 'application/json'}
data = {
    "name": "llama3.2",
    "stream": True
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Success")
    sys.exit(0)
else:
    print("Failed")
    print(response)
    sys.exit(1)