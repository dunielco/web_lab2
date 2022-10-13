def sqr_n(a, n):
    eps = 0.001
    xi = 1

    while True:
        xi_1 = (((n-1) * xi) + (a / (xi ** (n-1)))) / n
        if abs(xi_1 - xi) < eps:
            break
        xi = xi_1

    return xi_1

a = float(input('Введите число: '))
n = int(input('Введите степень: '))

if a < 0 or n <= 0:
    print('Неверные значения!')
    exit()

print('Корень равен:', end=' ')
print(sqr_n(a, n))

#   by dunielco