import requests

#response = requests.get("https://playground.learnqa.ru/api/something") несуществующий запрос
#print(response.status_code) показывает статус запроса
#print(response.text) показывает ответ запроса

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
#print(response.status_code) при изменении булевого значения показывает статус до редиректа и после
first_response = response.history[0] #история редиректов до последней страницы
second_response= response

print(first_response.url)
print(second_response.url)
