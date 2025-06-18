import requests
import json
headers = {
    "Authorization": "Bearer api_key",
    "Content-Type": "application/json",
    "use-case": "testing",
}
data = {"messages": [{"role": "user", "content": "Who is George Washington?"}], "temperature": 0.7 }
data = json.dumps(data)
url = f'https://localhost/rest/v2/azure/openai/deployments/gpt-4o-latest/chat/completions' #?api-version=2023-09-01-preview'
response = requests.post(url, headers = headers, data = data, verify=False)
pretty_json = json.loads(response.text)
print(json.dumps(pretty_json, indent = 2))
