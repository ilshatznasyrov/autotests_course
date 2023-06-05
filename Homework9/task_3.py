# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open(r'test_file/task_3.txt', 'r', encoding='utf8') as file:
    sum_list = [0]
    for i in file:
        if i == "\n":
            sum_list.append(0)
        else:
            sum_list[-1] += int(i.rstrip("\n"))
    sum_list.sort(reverse=True)
    three_most_expensive_purchases = sum(sum_list[0:3])


assert three_most_expensive_purchases == 202346
