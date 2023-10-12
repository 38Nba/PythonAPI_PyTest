import pytest
import requests


class TestFirstAPI:
    names = [("Nikita"), #проверка будет происходить три раза
             ("Sasha"),
             ("")]

    @pytest.mark.parametrize('name', names) #указываем имя переменной в которой будем передавать данные
    def test_hello_world(self, name): #добавили переменную имя в которой передается список с проверочными именами
        url = "https://playground.learnqa.ru/api/hello"
        data = {'name': name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Wrong response code" #если код не 200 получим такое сообщение

        response_dict = response.json()
        assert "answer" in response_dict, "There is no field 'answer' in the response" #проверяем имеется ли в словаре поле "answer", небходимо для того чтобы в дальнейшем к нему обпатиться

        if len(name) == 0:
            expected_response_text = "Hello, someone"
        else:
            expected_response_text = f"Hello, {name}" #ожидаемый текст ответа

        actual_response_text = response_dict["answer"] #реальный текст ответа
        assert expected_response_text == actual_response_text, "Actual text in the response is not correct" #сравниваем, если отличаются выводим ошибку
