"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def calc(first_number=1, second_number=1, operation=0):
    try:
        if first_number == 1 and second_number == 1 and operation == 0:
            print('')
        if operation == '+':
            print(f'{first_number}{operation}{second_number} = {first_number + second_number}')
        elif operation == '-':
            print(f'{first_number}{operation}{second_number} = {first_number - second_number}')
        elif operation == '*':
            print(f'{first_number}{operation}{second_number} = {first_number * second_number}')
        elif operation == '/':
            print(f'{first_number}{operation}{second_number} = {first_number / second_number}')
        else:
            print('Вы ввели не операцию, небходимо ввести +, -, *, / или 0 для выхода')
        operation = input('Введите операцию (+, -, *, / или 0 для выхода):')
        if operation == '0':
            return print('Программа завершена')
        else:
            first_number = int(input('Введите первое число:'))
            second_number = int(input('Введите второе число:'))
            calc(first_number, second_number, operation)
    except ZeroDivisionError:
        print('Делить на ноль нельзя!')
        calc(1, 1, 0)
    except ValueError:
        print('Вы ввели не число, исправтесь!')
        calc(1, 1, 0)


calc(1, 1, 0)