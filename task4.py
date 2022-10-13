def sqr_n(a, n):
    eps = 0.001
    a = float(a)
    n = int(n)
    xi = 1

    while True:
        xi_1 = (((n-1) * xi) + (a / (xi ** (n-1)))) / n
        if abs(xi_1 - xi) < eps:
            break
        xi = xi_1

    return xi_1

a = input('Введите число: ')
n = input('Введите степень: ')
print('Корень равен:', end=' ')
print(sqr_n(a, n))

#   by dunielco