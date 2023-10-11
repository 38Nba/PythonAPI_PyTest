import requests
headers = {"accept": "application/json"} #поиск по headers который отправляем вместе с запросом
response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=pending", headers=headers)
print(response.status_code) #статус кода
print(response.text) #ответ по headers который передаем
print(response.headers) #ответ по headers которые получаем
