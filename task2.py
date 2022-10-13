def check_div(nums, div_num):
    result = []
    for num in nums:
        if num % div_num == 0:
            result.append(num)
    return result

nums = []
print('Введите количество цифр, а затем значения: ')
for i in range(int(input())):
    nums.append(int(input()))

print('Делятся на 2:', end=' ')
print(check_div(nums, 2))
print('Делятся на 3:', end=' ')
print(check_div(nums, 3))
print('Делятся на 5:', end=' ')
print(check_div(nums, 5))

#   by dunielco