import requests

response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=available")
print(response.text)