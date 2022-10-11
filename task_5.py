# Задача 5 VERY HARD SORT необязательная
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. 
# Отсортировать элементы по возрастанию слева направо и сверху вниз.
def print_array(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print("{:4d}".format(array[i][j]), end = "")
        print()
def mas_in_list(array):
    list = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            list.append(array[i][j])
    return list
def sort_list(list):
    for k in range(len(list)-1):
        pos_max = 0
        for i in range(len(list)-k):
            if list[i] > list[pos_max]:
                pos_max = i
        temp = list[pos_max]
        list[pos_max] = list[len(list)-1-k]
        list[len(list)-1-k] = temp
def list_in_mas(list, massiv):
    k = 0 
    for i in range(len(massiv)):
        for j in range(len(massiv[i])):
            massiv[i][j] = list[k]
            k+=1
try:
    n = int(input('Введите количество строк: '))
    m = int(input('Введите количество столбцов: '))
    from random import randint
    mas = [[randint(-10, 10) for j in range(m)] for i in range(n)]
    print_array(mas)
    print('Sort massiv')
    arr = mas_in_list(mas)
    sort_list(arr)
    list_in_mas(arr, mas)
    print_array(mas)
except:
    print('Вводите только числа')