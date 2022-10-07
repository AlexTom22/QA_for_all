# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения(с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.
# def square(a):
#     p = a * 4
#     s = a * a
#     d = (a ** 2 + a ** 2) ** 0.5
#     return (p, s, d)
#
# print(square(3))


# # 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их
# # построчно в формате аргумент: значение. Например:
# # name: John
# # last_name: Smith
# # age: 35
# # position: webdeveloper
# def books(**kwargs):
#     for k, v in kwargs.items():
#         print(f"{k}: {v}")
#
#
# books(Id = 1, Autor = "Стив Джобс", Name = 'Про Apple')


# # 4.3. Используя лямбда - выражение, из списка
# # my_list = [20, -3, 15, 2, -1, -21]
# # создайте новый список, содержащий только положительные числа
# my_list = [20, -3, 15, 2, -1, -21]
# new_list = list(filter(lambda x: x > 0, my_list))
# print(new_list)


# # 4.4.Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# from functools import reduce
# my_list = [20, -3, 15, 2, -1, -21]
# print(my_list)
# print(reduce(lambda x, y: x*y, my_list))
# new_list = list(filter(lambda x: x > 0, my_list))
# print(new_list)
# print(reduce(lambda x, y: x*y, new_list))


# # 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
# # Примените эти функции в качестве методов в другом файле.
# from my_calc import *
# print(my_sum(2, 5))
# print(my_sub(2, 5))
# print(my_mul(2, 5))
# print(my_div(2, 5))

# ПОДСКАЗКИ
# # ==================================================================
# 4.1.
# from math import sqrt
# def square(side):
#   return (side*side, side*4, round(sqrt(side**2*2)))
#
#
#
#
# 4.2.
# def employee(**kwargs):
#     for k, v in kwargs.items():
#         print(f'{k}: {v}')
#
# employee(last_name='Popov', name='Max', age=40, position='web developer')
#
# 4.3. my_list = [20, -3, 15, 2, -1, -21]
#      print(list(filter(lambda x: x > 0, my_list)))
#
# 4.4
# # Условие этой задачи было понято по-разному из-за не совсем точной формулировки. Нужно было перемножить все тот же
# my_list, но если вы перемножали отфильтрованный лист - тоже ок)
# from functools import reduce
# print(reduce(lambda x, y: x*y, my_list))
#
# # Чтобы получить результат перемножения только положительных значений
# print(reduce(lambda x, y: x*y, [x for x in my_list if x > 0]))
#
# 4.5.
# #my_calc.py
# def add(x, y):
#     return x + y
#
#
# def remain(x, y):
#     return x % y
#
#
# def subtract(x, y):
#     return x - y
#
#
# def prod(x, y):
#     return x * y
#
#
# def divide(x, y):
#     try:
#         return x / y
#     except ZeroDivisionError:
#         return "Can't divide by zero"
#
#
# from my_file import *
#
# prod_res = prod(100, 20)
# print(res)
#
# div_res1 = divide(45, 9)
# print(div_res1)
#
# div_res2 = divide(5, 0)
# print(div_res2)
#
# add_res = add(585, 1987)
# print(add_res)
#
# remain_res = remain(541, 6)
# print(remain_res)
#
# sub_res = subtract(230, 149)
# print(sub_res)
#
#
# def tests():
#     assert add(5, 8) == 13, f'Wrong number, actual result is {sum_it(5, 8)}'
#     assert prod(10, 6) == 60, f'Wrong number, actual result is {prod(10, 6)}'
#     assert divide(10, 0) == "Can't divide by zero", "Shouldn't divide by zero"
#     assert subtract(85, 28) == 57,  f'Wrong number, actual result is {subtract(85, 28)}'
#     assert remain(9, 4) == 1, f'Wrong number, actual result is {remain(9, 4)}'
#
# tests()
#
#
