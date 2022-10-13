def rotate(num):
    num = int(num)
    num_str = [d for d in str(num)] #Перевод в строку
    num_str.reverse()   #Разворот строки
    if num < 0: #Работа с отрицательными числами
        num_str.insert(0, num_str.pop())
    return int(''.join(num_str))

#Вывод с вызовом функции
num = input('Введите число: ')
print(rotate(num))

#   by dunielco