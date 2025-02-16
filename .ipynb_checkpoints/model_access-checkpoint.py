import requests
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

response = requests.get(
    "https://api.groq.com/openai/v1/models",
    headers={"Authorization": f"Bearer {GROQ_API_KEY}"}
)

if response.status_code == 200:
    models = response.json().get("data", [])
    model_ids = [model["id"] for model in models]
    print(model_ids)
else:
    print(f"Error: {response.status_code}, {response.text}")
