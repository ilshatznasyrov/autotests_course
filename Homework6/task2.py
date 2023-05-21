# Нелокальные изменения
# Имеется функция global_function с локальной переменной msg = 1
# Ваша задача дополнить логику функции global_function следующим образом:
# global_function должна содержать в себе функцию local_function
# local_function должна изменить значение переменной msg на значение 2

def global_function():
  """
  Функция возвращает вложенную функцию local_function, изменяющую переменную msg на новое значение
  msg: исходная переменная
  :return: local_function - вложенная функция
  """
  msg = 1
  def local_function():
    """
    Функция изменяет глобальную переменную msg на новое значение и возвращает ее в измененном виде
    msg: исходная глобальная переменная
    :return: измененная глобальная переменная msg
    """
    # Здесь нужно написать код
    global msg
    msg = 2
    return msg
  return local_function()

global_function()


assert global_function() == 2, 'Значение переменной msg должно быть равно 2'
print('Все ок')
