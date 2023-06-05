# Напишите функцию segment
# На вход подается два кортежа с координатами точек (x1, y1), (x2, y2)

# В функции происходит проверка на корректность полученных данных.
# С помощью инструкции try/except as отлавливается исключение Exception. И если это исключение поймано,
# то функция возвращает текст исключения задом наперед (Нужно обратится к атрибуту экзепляра класса Exception)
# Если исключения не произошло, то функция возвращает сумму всех координат


# Здесь пишем код
def segment(first_tuple, second_tuple):
    """
    Функция принимает на вход два кортежа с координатами точек (x1, y1), (x2, y2)
    и проверяет полученные данные на корректность.
    С помощью инструкции try/except as отлавливается исключение Exception.
    :param first_tuple: первый кортеж с координатами точек
    :param second_tuple: второй кортеж с координатами точек
    :return: если исключение поймано, то функция возвращает текст исключения задом наперед.
    Если исключения не произошло, то функция возвращает сумму всех координат
    """
    try:
        return first_tuple[0] + first_tuple[1] + second_tuple[0] + second_tuple[1]
    except TypeError as error:
        return error.args[0][-1::-1]


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    ((2, 3), (4, 5)),
    ((2, -3), (4, 5)),
    ((2, 3), ('4', 5)),
    (('a', 3), (4, 5)),
]

test_data = [
    14,
    8,
    "'rts' dna 'tni' :+ rof )s(epyt dnarepo detroppusnu",
    'rts ot )"tni" ton( rts etanetacnoc ylno nac']


for i, d in enumerate(data):
    assert segment(*d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')