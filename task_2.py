# задача 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z  для всех значений предикат.
def left_side (X, Y, Z):
    res = not(X or Y or Z)
    return res
def right_side(X, Y, Z):
    res = not(X) and not(Y) and not(Z)
    return res
def convert_boolian(num):
    if num == 0: 
        res = False
    else:
        res = True
    return res
try:
    for i in range(2):
        for j in range(2):
            for k in range(2):
                x = convert_boolian(i)
                y = convert_boolian(j)
                z = convert_boolian(k)
                if left_side(x, y, z) == right_side(x, y, z):
                    res = 'для данных значений пердикатов утверждение истино'
                else:
                    res = 'для данных значений пердикатов утверждение ложно'
                print(f'\n {i}  {j}  {k}  {res}')
except:
    print('что-то пошло не так')