from json.decoder import JSONDecodeError #если выдает список ошибок можно импортировать декодер
import requests

response = requests.get("https://playground.learnqa.ru/api/get_text")
try:
    parsed_response_text = response.json()
    print(parsed_response_text)
except JSONDecodeError:
    print("Response is not a JSON format")