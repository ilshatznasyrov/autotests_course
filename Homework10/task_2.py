# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    """
    Функция делит и возвращает результат деления
    :param arg1: последовательность чисел, первое число делимое, остальные - делители
    :return: результат деления
    """
    try:
        division = arg1[0]
        for i in arg1[1:]:
            division /= i
        return division
    except TypeError:
        print('Необходимо число!')
    except ZeroDivisionError:
        print('Нельзя делить на 0!')


@pytest.mark.smoke
def test_int():
    """
    Проверка - результат целое число
    """
    assert all_division(8, 4) == 2


@pytest.mark.smoke
def test_float():
    """
    Проверка - результат дробное число
    """
    assert all_division(3, 2) == 1.5


@pytest.mark.acceptance
def test_zero():
    """
    Проверка деление на 0
    """
    assert all_division(5, 0) is None


def test_divider_letter():
    """
    Проверка делитель не число
    """
    assert all_division(7, 'x') is None


def test_dividend_letter():
    """
    Проверка делимое не число
    """
    assert all_division('y', 8) is None