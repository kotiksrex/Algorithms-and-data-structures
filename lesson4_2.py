# Функция поиска i-го простого числа,
# используя алгоритм «Решето Эратосфена»

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

#числа до 40
#1000 loops, best of 5: 8.91 usec per loop

#числа до 100
#1000 loops, best of 5: 23.9 usec per loop

#числа до 10000
#1000 loops, best of 5: 3.67 msec per loop




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
    #print('')

#числа до 40
#1000 loops, best of 5: 193 usec per loop

#числа до 100
#1000 loops, best of 5: 275 usec per loop

#числа до 10000
#1000 loops, best of 5: 925 nsec per loop



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

#числа до 100
#1000 loops, best of 5: 73 usec per loop

#числа до 10000
#1000 loops, best of 5: 11.6 msec per loop



import cProfile

cProfile.run('eratosthenes_sieve(100)')

cProfile.run('primeNUM(2, 100)')

cProfile.run('approach3(100)')


   #      6 function calls in 0.000 seconds

   #   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#    1    0.000    0.000    0.000    0.000 lesson4_2.py:4(eratosthenes_sieve)


      #   4 function calls in 0.000 seconds

  #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)

   #     1    0.000    0.000    0.000    0.000 lesson4_2.py:33(primeNUM)



     #    29 function calls in 0.000 seconds


   #ncalls  tottime  percall  cumtime  percall filename:lineno(function)

     #   1    0.000    0.000    0.000    0.000 lesson4_2.py:57(approach3)
     #  25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

#В моем варианте функция с использованием алгоритма решета Эратосфена оказалась самой быстрой, хотя сам алгоритм
# поиска простых чисел не самый удачный. Выполнение функции approach3, вероятно, замедлено за счет метода append

