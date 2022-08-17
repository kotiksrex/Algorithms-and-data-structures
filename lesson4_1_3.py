from random import random
M = 10000
N = 10000
a = []
for i in range(N):
    b = []
    for j in range(M):
        n = int(random()*200)
        b.append(n)
       # print('%4d' % n,end='')
    a.append(b)
    #print()

mx = -1
for j in range(M):
    mn = 200
    for i in range(N):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
#print("Максимальный среди минимальных: ", mx)

#для матрицы 4х4
#1000 loops, best of 5: 9.2 nsec per loop

#для матрицы 10000х10000
#1000 loops, best of 5: 22.9 nsec per loop

#Вывод: создание рандомной матрицы с помощью функции или генератора значительно сокращает время
# значительно сокращает время выполнения программы на больших числах.


