# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.


from random import random

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

#для матрицы 4х4
#1000 loops, best of 5: 9.3 nsec per loop

#для матрицы 10000х10000
#1000 loops, best of 5: 9.3 nsec per loop

#Вывод: создание рандомной матрицы с помощью функции или генератора значительно сокращает время
# значительно сокращает время выполнения программы на больших числах.


