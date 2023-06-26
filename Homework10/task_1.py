# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string

# Здесь пишем код
def generate_random_name():
    """
        Геренатор двух слов из латинских букв длиной от 1 до 15 символов
    """
    letters = string.ascii_lowercase
    while True:
        word = ' '.join(''.join(random.choices(letters, k=random.randint(1, 15))) for i in range(2))
        yield word

gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))