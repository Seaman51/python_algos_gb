"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from random import randint
from timeit import timeit
import cProfile

array = [randint(0, 77) for el in range(777)]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    numb = max(array, key=array.count)
    return f'Чаще всего встречается число {numb}, оно появилось в массиве {array.count(numb)} раз(а)'


print(func_1())
print(func_2())
print(func_3())
cProfile.run("func_1()")
cProfile.run("func_2()")
cProfile.run("func_3()")
print(timeit('func_1()', setup='from __main__ import func_1', number=10000))
print(timeit('func_2()', setup='from __main__ import func_2', number=10000))
print(timeit('func_3()', setup='from __main__ import func_3', number=10000))
"""
при array = [randint(0, 77) for el in range(77)]

Чаще всего встречается число 72, оно появилось в массиве 3 раз(а)
Чаще всего встречается число 72, оно появилось в массиве 3 раз(а)
Чаще всего встречается число 72, оно появилось в массиве 3 раз(а)
         81 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_4.py:19(func_1)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       77    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         160 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_4.py:31(func_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
       77    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
       77    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


         6 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_4.py:43(func_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


0.8534248
0.8539796000000001
0.7921689999999999

Process finished with exit code 0
C:\Python3\python.exe "D:/Test/python_algos_gb/Урок 4. Практическое задание/task_4.py"
Чаще всего встречается число 44, оно появилось в массиве 17 раз(а)
Чаще всего встречается число 44, оно появилось в массиве 17 раз(а)
Чаще всего встречается число 44, оно появилось в массиве 17 раз(а)
         781 function calls in 0.009 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.009    0.009 <string>:1(<module>)
        1    0.000    0.000    0.009    0.009 task_4.py:19(func_1)
        1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
      777    0.008    0.000    0.008    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         1560 function calls in 0.008 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.008    0.008 <string>:1(<module>)
        1    0.000    0.000    0.008    0.008 task_4.py:31(func_2)
        1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
      777    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
      777    0.007    0.000    0.007    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


         6 function calls in 0.007 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.007    0.007 <string>:1(<module>)
        1    0.000    0.000    0.007    0.007 task_4.py:43(func_3)
        1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
        1    0.007    0.007    0.007    0.007 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


73.5553459
74.83979409999999
77.7163941

Process finished with exit code 0

В определенном диапазоне третья функция быстрее, но не более.
"""
