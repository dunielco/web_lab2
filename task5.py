def check_prime(num):
    if num % 2 == 0:    #Проверка на чётность
        return num == 2
    div = 3     #Проход по нечётным числам
    while div ** 2 <= num and num % div != 0:   #Проверка на делимость
        div += 2
    return div ** 2 > num

#Ввод
num = int(input('Введите число: '))
#Проверка на корректность
if num < 0 or num > 100000:
    print('Выход за пределы условия!')
    exit()
else:   #Вызов функции
    print('Простое? ', end='')
    print(check_prime(num))

#   by dunielco