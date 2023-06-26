# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

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

@pytest.mark.parametrize('x, y, division',
                         [pytest.param(5, 2.5, 2, marks=pytest.mark.smoke),
                          pytest.param(0, 7, 0, marks=pytest.mark.skip)])
def test_int(x, y, division):
    """
    Проверка - результат целое число
    """
    assert all_division(x, y) == division





