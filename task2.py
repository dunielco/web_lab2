def check_div(nums, div_num):
    result = [] #Массив чисел
    for num in nums:    #Проход по исходному массиву
        if num % div_num == 0:  #Проверка на делимость на нужную цифру
            result.append(num)  #Запись этого числа в массив
    return result

#Исходный массив и запись в него
nums = []
print('Введите количество цифр, а затем значения: ')
for i in range(int(input())):
    nums.append(int(input()))

#Вывод и вызов функции
print('Делятся на 2:', end=' ')
print(check_div(nums, 2))
print('Делятся на 3:', end=' ')
print(check_div(nums, 3))
print('Делятся на 5:', end=' ')
print(check_div(nums, 5))

#   by dunielco