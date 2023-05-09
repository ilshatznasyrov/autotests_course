# Задача со ЗВЁЗДОЧКОЙ. Решать НЕ обязательно.
# Программа получает на вход натуральное число num.
# Программа должна вывести другое натуральное число, удовлетворяющее условиям:
# Новое число должно отличаться от данного ровно одной цифрой
# Новое число должно столько же знаков как исходное
# Новое число должно делиться на 3
# Новое число должно быть максимально возможным из всех таких чисел
# Например (Ввод --> Вывод) :
#
# 379 --> 879
# 15 --> 75
# 4974 --> 7974

def max_division_by_3(num):
    # Здесь нужно написать код
    num_lst = []
    for char in str(num):
        num_lst.append(int(char))
    result = []
    for idx, el in enumerate(num_lst):
        for i in range(0, 10):
            num_lst[idx] = i
            if sum(num_lst) % 3 == 0:
                result.append(num_from_list(num_lst))
                num_lst[idx] = el
            else:
                num_lst[idx] = el
    new_num = max(result)
    return new_num

def num_from_list(lst_of_num):
    lst_of_num.reverse()
    num = 0
    for i, el in enumerate(lst_of_num):
        num += el * 10 ** i
    lst_of_num.reverse()
    return num


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    379, 810, 981, 4974, 996, 9000, 15, 0, 9881, 9984, 9876543210, 98795432109879543210
]

test_data = [
    879, 870, 987, 7974, 999, 9900, 75, 9, 9981, 9987, 9879543210, 98798432109879543210
]


for i, d in enumerate(data):
    assert max_division_by_3(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
