import sys

print(sys.version, sys.platform)
#3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] win32

#Для анализа используем два варианта решения 9-той задачи из 4-го урока:
# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random
#Вариант 1

M = 10000
N = 10000
a = []
for i in range(N):
    b = []
    for j in range(M):
        n = int(random() * 200)
        b.append(n)
    # print('%4d' % n,end='')
    a.append(b)
    # print()

mx = -1
for j in range(M):
    mn = 200
    for i in range(N):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
# print("Максимальный среди минимальных: ", mx)

#print(sys.getsizeof(a))

#sum_member = sys.getsizeof(M) + sys.getsizeof(N) + sys.getsizeof(a) \
            # + sys.getsizeof(b) + sys.getsizeof(n) + sys.getsizeof(mx) + sys.getsizeof(mn)

#print('В программе задействовано байт памяти: {}'.format(sum_member))
# В программе задействовано байт памяти: 175364

#Вариант 2

N = 10000
M = 10000
A = [[0] * M for i in range(N)]
for i in range(N):
    for j in range(M):
        A[i][j] = int(random() * 100)
        #print(A[i][j], end=' ')
    #print()

mx = -1
for j in range(M):
    mn = 100
    for i in range(N):
        if A[i][j] < mn:
            mn = A[i][j]
    if mn > mx:
        mx = mn
#print("Максимальный элемент среди минимальных: ", mx)

sum_member = sys.getsizeof(M) + sys.getsizeof(N) + sys.getsizeof(A) \
              + sys.getsizeof(n) + sys.getsizeof(mx) + sys.getsizeof(mn)

print('В программе задействовано байт памяти: {}'.format(sum_member))
#В программе задействовано байт памяти: 87748

#Вывод: создание рандомной матрицы с помощью генератора значительно сокращает  как время
#  выполнения программы (на больших числа), так и объем используемой памяти.