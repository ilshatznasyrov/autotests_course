import math

# Задача 1
print('---Задача 1---')
side = 3
perimeter = 4 * side
area = side * side
diagonal = math.sqrt(2) * side
print('Периметр квадрата равен: ', perimeter)
print('Площадь квадрата равна: ', area)
print('Диагональ квадрата равна: ', round(diagonal, 2))

# Задача 2
print('\n---Задача 2---')
# Дискриминант уравнения по условиям задачи больше 0
a = 4
b = 7
c = -56
discriminant = b ** 2 - 4 * a * c
x_1 = (-b + math.sqrt(discriminant)) / (2 * a)
x_2 = (-b - math.sqrt(discriminant)) / (2 * a)
print(f'Корни квадратного урравнения: {round(x_1, 2)} и {round(x_2, 2)}.')

# Задача 3
print('\n---Задача 3---')
name = 'Ilshat'
surname = 'Nasyrov'
# Создадим новые переменные new_name и new_surname в которые запишем списки из строк name и surname
new_name = list(name)
new_surname = list(surname)
# Поменяем местами первые два символа из первой строки на первые два символа строки surname
new_name[0], new_name[1] = surname[0], surname[1]
# Поменяем местами первые два символа из второй строки на первые два символа строки name
new_surname[0], new_surname[1] = name[0], name[1]
# Запишем в новую переменную, преобразованные методом join() обработанные списки
my_name_is = ''.join(new_name) + ' ' + ''.join(new_surname)
# Используем title() для вывода каждого слова с заглавной буквы, т.к. использовал имя и фамилию
print(my_name_is.title())

# Задача 4
print('\n---Задача 4---')
dir = 'C:\Program Files\errors.log'
# Разобъем строку на список из отдельных элементов без слешей
new_dir = dir.split('\\')
# Запишем в новую переменную название файла до точки (без расширения) взятое из посленего элемента списка
file = new_dir[-1].split('.')[0]
# Запишем в новую переменную название диска взятое из первого элемента списка
disk = new_dir[0].split(':')[0]
# Запишем в новую переменную название корневой папки взятое из второго элемента списка (следующего после названия диска)
folder = new_dir[1]
print(f'Название файла: {file}, название диска: {disk}, корневая папка: {folder}.')

# Задача 5
print('\n---Задача 5---')
a = 3
b = 7
print(f'{a} + {b} = {a + b}')
print(f'{a} * {b} = {a * b}')

# Задача 6
print('\n---Задача 6---')
text = 'Тёплые деньки'
new_text = text[::2]
print(new_text)

# Задача 7
print('\n---Задача 7---')
# Длина первой строки по условиям задачи 3 символа 'brick quz jmpy veldt whangs fox'
# Вторая строка точно содержит символы первой строки в любом порядке
first_string = 'wtf'
second_string = 'brick quz jmpy veldt whangs fox '
# Создаем массив, в который положем найденные во второй строке индексы символов соответствующих симовлам первой строки
slice = []
slice.append(second_string.find(first_string[0]))
slice.append(second_string.find(first_string[1]))
slice.append(second_string.find(first_string[2]))
# Отсортируем массив по порядку, чтобы перым лежало наименьшее из найденных значений, а последним - наибольшее
slice.sort()
# Запишем наименьшее значение для среза
result_min = slice[0]
# Запишем наибольшее значение для среза, с учетом +1 чтобы это значение тоже выводилось в срезе
result_max = slice[-1] + 1
# Найдем срез минимальной длины во второй строке, который содержит все символы первой строки
print(f'Срез мининмальной длины: {second_string[result_min:result_max]}')