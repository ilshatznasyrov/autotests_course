# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest



def all_division(*arg1):
    """
        Функция делит и возвращает результат деления
        :param arg1: последовательность чисел, первое число делимое, остальные - делители
        :return: результат деления
    """
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.usefixtures('print_time')
class Test:


    def test_int(self):
        """
        Проверка - результат целое число
        """
        assert all_division(8, 4) == 2

    @pytest.mark.usefixtures('print_work_time')
    def test_float(self):
        """
        Проверка - результат дробное число
        """
        assert all_division(3, 2) == 1.5

    def test_zero(self):
        """
        Проверка деление на 0
        """
        assert all_division(5, 0) is None

