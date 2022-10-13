def check_prime(num):
    if num % 2 == 0:
        return num == 2
    div = 3
    while div ** 2 <= num and num % div != 0:
        div += 2
    return div * div > num


num = int(input('Введите число: '))
if num < 0 or num > 100000:
    print('Выход за пределы условия!')
    exit()
else:
    print('Простое? ', end='')
    print(check_prime(num))

#   by dunielco