import functools    #Библиотека для декоратора

@functools.cache    #Кэширование
def factorial(num):
    return num * factorial(num-1) if num else 1 #Вычисление факториала

#Ввод и вызов функции
num = int(input('Число: '))
print('Факториал: ', end='')
print(factorial(num))

#   by dunielco