"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""
from timeit import timeit

def simple(i):
    # O(n^2)
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n

def eratosfen(i):
    # O(n log(log n))
    n = 2
    l = 10000
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n*2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    return [p for p in sieve if p != 0][i-1]

i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(eratosfen(i))

print(timeit('simple(1000)', setup='from __main__ import simple', number=10000))
print(timeit('eratosfen(1000)', setup='from __main__ import eratosfen', number=10000))

"""
C:\Python3\python.exe "D:/Test/python_algos_gb/Урок 4. Практическое задание/task_5.py"
Введите порядковый номер искомого простого числа: 10
29
29
0.15878099999999984
36.5186498

Process finished with exit code 0
C:\Python3\python.exe "D:/Test/python_algos_gb/Урок 4. Практическое задание/task_5.py"
Введите порядковый номер искомого простого числа: 100
541
541
20.8734446
32.752459599999995

Process finished with exit code 0"""

C:\Python3\python.exe "D:/Test/python_algos_gb/Урок 4. Практическое задание/task_5.py"
Введите порядковый номер искомого простого числа: 1000
7919
7919
3450.1788229999997
35.45107480000024

Process finished with exit code 0