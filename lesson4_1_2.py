"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import random


def print_matrix(matrix):
    for line in matrix:
        for item in line:
            print(f"{item:>4}", end="")
        print()
    print()


def generate_matrix(m, n):
    return [[random.randint(1, 100) for _ in range(n)] for _ in range(m)]


def get_min_elements_in_columns(matrix):
    min_elements = matrix[0]
    for line in matrix[1:]:
        for i, element in enumerate(line):
            if min_elements[i] > element:
                min_elements[i] = element

   # print("min_elements:", min_elements)
    return min_elements


def find_max_element(matrix):
    min_elements = get_min_elements_in_columns(matrix)
    max_element = min_elements[0]
    for element in min_elements[1:]:
        if max_element < element:
            max_element = element

   # print("Max element:", max_element)


M = generate_matrix(10000, 10000)
#print_matrix(M)
find_max_element(M)

#для матрицы 4х4
#1000 loops, best of 5: 9.2 nsec per loop

# для матрицы 10000х10000
#1000 loops, best of 5: 9.3 nsec per loop

#Вывод: создание рандомной матрицы с помощью функции или генератора значительно сокращает время
# значительно сокращает время выполнения программы на больших числах.
