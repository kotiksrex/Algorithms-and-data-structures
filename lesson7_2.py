# https://pythobyte.com/merge-sort-in-python-59c4dd32/
#2. Отсортируйте по возрастанию методом слияния
# одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.


import random


array_ = [i for i in range(50)]  # создание рандомного массива от 0 до 50 не включительно с помощью генератора
random.shuffle(array_)  # метод shuffle для перемешивания значений в массиве

print(array_)

def merge(array, left_index, right_index, middle):
    # сделаем копии массивов, которые будем объединять

    # увеличиваем на 1
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]

    # переменные для определения текущего положения в массивах

    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # цикл прохождения по копиям
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        #если в левой копии имеется меньший элемент помещаем его в отсотрир часть и двигаемся дальше
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1

        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        # двигаемся вперед в отсотрированной части
        sorted_index = sorted_index + 1

    # когда закончились элементы либо в left_copy, либо в right_copy.
    # пройдемся по оставшимся элементам и добавим их 
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1


def merge_sort(array, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    merge_sort(array, left_index, middle)
    merge_sort(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)


merge_sort(array_, 0, len(array_) -1)

print(array_)
