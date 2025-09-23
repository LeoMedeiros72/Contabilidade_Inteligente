import requests

API_URL = "http://localhost:3000/api/v1/prediction/0e5764d1-1234-4b88-8fb0-ca07c3f9804f"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()
    
output = query({
    "question": "Pode me ajudar? Baseado no seu banco de dados, quais as 3 menores empresas que você possui?",
})

print(output)
