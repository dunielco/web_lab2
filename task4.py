def sqr_n(a, n):
    eps = 0.001 #Точность
    xi = 1  #Начальное значение

    while True:
        xi_1 = (((n-1) * xi) + (a / (xi ** (n-1)))) / n #Расчёт по формуле
        if abs(xi_1 - xi) < eps:    #Проверка точности
            break
        xi = xi_1   #Проход по i дальше
    return xi_1

#Ввод значений
a = float(input('Введите число: '))
n = int(input('Введите степень: '))

#Проверка на корректность
if a < 0 or n <= 0:
    print('Неверные значения!')
    exit()

#Вывод результатов
print('Корень равен:', end=' ')
print(sqr_n(a, n))

#   by dunielco