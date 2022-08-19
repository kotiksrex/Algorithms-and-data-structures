import sys


def show_size(x, level=0):
    ''' функция сложения всех затрат памяти
        и возврат общей суммы затраченной памяти '''
    size_par = sys.getsizeof(x)
    print('\t' * level, f'type={type(x)}, size={size_par}, object={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                size_par = size_par + sys.getsizeof(key)
                show_size(value, level + 1)
                size_par = size_par + sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)
                size_par = size_par + sys.getsizeof(item)
    return size_par

def eratosthenes_sieve(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2

            while j < n:
                sieve[j] = 0
                j += i

    return [i for i in sieve if i != 0]

show_size(eratosthenes_sieve)

# type=<class 'function'>, size=136, object=<function eratosthenes_sieve at 0x000001E7F14A2790>

# Функция поиска i-го простого числа,
# без алгоритма «Решето Эратосфена»

def primeNUM(min, max):
    global j
    if min == 1:
        #print('')
        min += 1
    for i in range(min, max + 1):
        for j in range(2, i + 1):
            if i % j == 0:  # Судите, могу ли я быть делимым
                break  # Выход из цикла for
        if j == i:  # Если j равно i, i - простое число
            return i

show_size(primeNUM)

def approach3(givenNumber):
    # Initialize a list
    primes = []

    for possiblePrime in range(2, givenNumber + 1):

        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)

    return (primes)


show_size(approach3)

# type=<class 'function'>, size=136, object=<function eratosthenes_sieve at 0x000001AA76672820>
# type=<class 'function'>, size=136, object=<function primeNUM at 0x000001AA766728B0>
# type=<class 'function'>, size=136, object=<function approach3 at 0x000001AA76672940>

#Все три функции равнозначны по объему занимаемой памяти
