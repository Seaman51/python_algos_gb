"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from timeit import timeit
import cProfile

# Рекурсия
def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)

# Цикл
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num

# Срез
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

print('Пример №1')
enter_num = int(input('Введите целое число: '))
revers(enter_num, revers_num=0)
revers_2(enter_num, revers_num=0)
revers_3(enter_num)

print('Число наоборот на рекурсиях: ', timeit(f'revers({enter_num})',
        setup='from __main__ import revers', number=10000)
      )
print('Число наоборот на циклах: ', timeit(f'revers_2({enter_num})',
        setup='from __main__ import revers_2', number=10000)
      )
print('Число наоборот на срезах: ', timeit(f'revers_3({enter_num})',
        setup='from __main__ import revers_3', number=10000)
      )

cProfile.run('revers(7777777)')
cProfile.run('revers_2(7777777)')
cProfile.run('revers_3(7777777)')

"""
C:\Python3\python.exe "D:/Test/python_algos_gb/Урок 4. Практическое задание/task_3.py"
Пример №1
Введите целое число: 213482651238768
Число наоборот на рекурсиях:  0.0395941999999998
Число наоборот на циклах:  0.02600220000000064
Число наоборот на срезах:  0.0038688000000002276
         11 function calls (4 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
      8/1    0.000    0.000    0.000    0.000 task_3.py:16(revers)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:26(revers_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:34(revers_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



Process finished with exit code 0
Лучшее срез!
"""