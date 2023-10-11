import requests

payload = {"name": "MAX"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
parsed_response_text = response.json()

print(parsed_response_text["answer"])