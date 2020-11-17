"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""

from random import random
from statistics import median
import heapq


def median1(l):
    nl = []
    heapq.heapify(nl)
    for i in range(len(l) // 2 + 1):
        heapq.heappush(nl, l[i])
    for i in range(len(l) // 2 + 1, len(l)):
        if l[i] > nl[0]:
            heapq.heapreplace(nl, l[i])
    return nl[0]


m = 2 * int(input('Построим массив длиной 2m + 1. Введите m ')) + 1

lst = [int(random() * 100) for i in range(m)]

print(lst)
print(median1(lst))
print(median(lst))  # для проверки

"""
встроенная функция быстрее
"""
