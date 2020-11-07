"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit


def func_1(nums):
    """O(n) - линейная сложность"""
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    """O(n) - линейная сложность"""
    return [i for i, el in enumerate(nums) if el % 2 == 0]


# 777
nums = [el for el in range(777)]
print('section 777')
print(
    timeit(
        "func_1(nums)",
        setup="from __main__ import func_1, nums",
        number=1000
    )
)

print(
    timeit(
        "func_2(nums)",
        setup="from __main__ import func_2, nums",
        number=1000
    )
)
# 777 77
nums = [el for el in range(77777)]
print('section 777 77')
print(
    timeit(
        "func_1(nums)",
        setup="from __main__ import func_1, nums",
        number=1000
    )
)

print(
    timeit(
        "func_2(nums)",
        setup="from __main__ import func_2, nums",
        number=1000
    )
)

# 7 777 777
nums = [el for el in range(1777777)]
print('section 1 777 777')
print(
    timeit(
        "func_1(nums)",
        setup="from __main__ import func_1, nums",
        number=1000
    )
)

print(
    timeit(
        "func_2(nums)",
        setup="from __main__ import func_2, nums",
        number=1000
    )
)

"""
C:\Python3\python.exe "D:/Test/python_algos_gb/Урок 4. Практическое задание/task_1.py"

section 777
0.11903970000000001
0.06772019999999998
section 777 77
7.349302
6.8873182
section 1 777 777
186.8962069
172.65546379999998

Генераторные выражения выполняются быстрее, чем код на цикле, однако данное
различие имеет смысл только в диапазоне низкого количества элементов
массива, при его возрастании это различие сводится к минимуму

Красоту вижу только в лаконичности!

section 777
0.11903970000000001/0.06772019999999998 = 1,75
section 777 77
7.349302/6.8873182 = 1,07
section 1 777 777
186.8962069/172.65546379999998 = 1,08


Process finished with exit code 0
"""
