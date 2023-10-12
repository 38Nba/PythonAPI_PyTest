class TestExamples:
    def test_check_math(self): #без приставки test в названии функции тест не сработает
        a = 5
        b = 9
        expected_sum = 11
        assert a + b == expected_sum, f"Sum of variables a and b is not equal to {expected_sum}" #вывод ошибки, если ответ неверен

    def test_check_math2(self):
        a = 5
        b = 9
        expected_sum = 14
        assert a + b == expected_sum, f"Sum of variables a and b is not equal to {expected_sum}"

# для запуска вывод в консоли  python -m pytest test_examples.py -k "test_check_math"