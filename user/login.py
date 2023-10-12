import requests

payload = {
  "id": 1124,
  "username": "Test",
  "firstName": "Testov",
  "lastName": "Testovich",
  "email": "testi@mail.ru",
  "password": "qwerty1",
  "phone": "79112223355",
  "userStatus": 0
}
response1 = requests.post("https://petstore.swagger.io/v2/user", data=payload)

cookie_value = response1.cookies.get("auth_cookie")

cookies = {}
if cookie_value is not None:
  cookies.update({"auth_cookie": cookie_value})




response2 = requests.get("https://petstore.swagger.io/v2/user/login?username=Test&password=qwerty", cookies=cookies)

print(response2.text)
#print(dict(response.cookies)) вывод куки в ответ
