# задача 4 HARD необязательная Напишите простой калькулятор, который считывает с пользовательского ввода три строки: 
# первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") 
# и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.

try:
    num1 = float(input('Введите первое число: '))
    num2 = float(input('Введите второе число: '))
    operation = input('Введите знак операции: ')
    if operation == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operation == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    elif operation == '*':
        print(f'{num1} * {num2} = {num1 * num2}')
    elif operation == '/':
        if num2 != 0:
            print(f'{num1} / {num2} = {num1 / num2}')
        else:
            print('На ноль делить нельзя!')
    elif operation == 'mod':
        if num2 != 0:
            print(f'{num1} mod {num2} = {num1 % num2}')
        else:
            print('На ноль делить нельзя!')
    elif operation == 'pow':
        print(f'{num1} pow {num2} = {num1 ** num2}')
    elif operation == 'div':
        if num2 !=0:
            print(f'{num1} div {num2} = {num1 // num2}')
        else:
            print('На ноль делить нельзя!')
    else:
        print('Такой оперции ещё нет')
except:
    print('Вводите числа')