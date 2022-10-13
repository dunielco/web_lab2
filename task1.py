def palindrome(num):
    num = int(num)
    copy_num = num
    check = 0
    while(num != 0):
        digit = num % 10
        check = check * 10 + digit
        num = int(num / 10)
    return check == copy_num

print(palindrome(input()))

#   by dunielco