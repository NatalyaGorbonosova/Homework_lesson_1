# задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#  и проверяет, является ли этот день выходным.
try:
    day_number = int(input('Введите номер дня недели: '))
    if day_number > 0 and day_number < 8:
        if day_number == 6 or day_number == 7:
            print('это выходной')
        else:
            print('это будний день')
    else:
        print('введите число от 1 до 7')
except:
    print('Введите число')


