# задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), и выдаёт номер четверти плоскости,
#  в которой находится эта точка (или на какой оси она находится).
try:
    x = int(input('Введите координату Х: '))
    y = int(input('Введите координату Y: '))
    if x > 0:
        if y > 0:
            print('Первая четверть')
        elif y < 0:
            print('Четвертая четверть')
        else:
            print('Лежит на оси Х')
    elif x < 0:
        if y > 0:
            print('Вторая четверть')
        elif y < 0:
            print('Третья четверть')
        else:
            print('Лежит на оси Х')
    elif x == 0:
        if y == 0:
            print('Начало координат')
        else:
            print('Лежит на оси Y')
except:
    print('Вводите только числа')