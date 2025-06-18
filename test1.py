import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="api_key", 
    api_version="2024-06-01",
    azure_endpoint="https://localhost/rest/v2/azure/",
    default_headers={"use-case":"testing"},
)

response = client.chat.completions.create(
    model="gpt-4o-latest",
    messages=[{"role": "user", "content": "Who is George Washington?"}],
    temperature=0.7,
)

print(response)
