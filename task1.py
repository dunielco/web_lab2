def palindrome(num):
    copy_num = num  #Сохранение первоначального числа
    check = 0   #Переменная для записи числа наоборот
    while(num != 0):
        digit = num % 10    #Запись последней цифры
        check = check * 10 + digit  #Добавление цифр в конец обратного числа
        num = int(num / 10) #Проход по первоначальному числу
    return check == copy_num

#Ввод числа и вызов функции
num = int(input('Введите число: '))
print(palindrome(num))

#   by dunielco