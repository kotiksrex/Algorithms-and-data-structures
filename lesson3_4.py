# 4. Определить, какое число в массиве встречается чаще всего.

from random import random

N = 15
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 20)
print(arr)

elem = arr[0]
max_freq = 1
for i in range(N - 1):
    freq = 1
    for k in range(i + 1, N):
        if arr[i] == arr[k]:
            freq += 1
    if freq > max_freq:
        max_freq = freq
        elem = arr[i]

if max_freq > 1:
    print(f' {max_freq} раз(а) встречается число {elem} ')
else:
    print('Все элементы уникальны')
