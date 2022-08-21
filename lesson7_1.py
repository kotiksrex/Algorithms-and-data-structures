#1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный
#массив, заданный случайными числами на промежутке [-100; 100). Выведите на
#экран исходный и отсортированный массивы. Сортировка должна быть реализована в
#виде функции. По возможности доработайте алгоритм (сделайте его умнее).


import random
from timeit import timeit

array_ = [i for i in range(-100, 100)]  # создание рандомного массива от 0 до 9 с помощью генератора
random.shuffle(array_)  # метод shuffle для перемешивания значений в массиве

print(array_)

NUMBER_EXECUTIONS = 1000


# заменила while на for

def bubble(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


bubble(array_)
print(array_)


# код из урока
def bubble1(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1


bubble1(array_)
print(array_)

time1 = timeit(f'bubble({array_})',
               setup='from __main__ import bubble',
               number=NUMBER_EXECUTIONS)
time2 = timeit(f'bubble1({array_})',
               setup='from __main__ import bubble1',
               number=NUMBER_EXECUTIONS)
print(f'тестовое время выполнений функции bubble равно {round(time1, 3)}')
print(f'тестовое время выполнений функции bubble1 равно {round(time2, 3)}')

#тестовое время выполнений функции bubble равно 0.819
#тестовое время выполнений функции bubble1 равно 0.852
#Вывод: сортировка пузырьком на циклах for работает немного быстрее, чем на while