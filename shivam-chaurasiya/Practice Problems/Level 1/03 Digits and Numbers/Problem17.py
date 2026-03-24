# Count Even Digits in a Number
# Write a program that takes a 4-digit number as input and counts how many of its digits are even, then displays the count.

num = int(input('Enter a 4-digit number: '))    # 4567
n = num
# count = 0
# while num > 0:
#     r = num % 10
#     if r % 2 == 0:
#         count+=1
#     num = num // 10
# print(f'Number {n} have {count} Even Digits')

count = 0
last_digit = num % 10           # 7
if last_digit % 2 == 0:
    count+=1

print(num)
third_digit = (num // 10) % 10  # 6
num = num // 10                 # 456
if third_digit % 2 == 0:
    count+=1

second__digit = (num // 10) % 10
num = num // 10
if second__digit % 2 == 0:
    count+=1
    
first_digit = (num // 10) % 10
num = num // 10
if first_digit % 2 == 0:
    count+=1

print(f'Number {n:04d} have {count} Even Digits')