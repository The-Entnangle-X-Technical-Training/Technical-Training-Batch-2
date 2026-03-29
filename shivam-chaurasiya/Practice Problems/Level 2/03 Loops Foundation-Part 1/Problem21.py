# Find Largest Digit in a Number
# Write a program that takes a number and finds the largest digit in it using a loop.

num = int(input('Enter a number: ')) # 153
original_num = num
largest_num = 0

while num > 0:
    r = num % 10
    if r > largest_num:
        largest_num = r
    num = num // 10

print(f'The largest digit in {original_num} is {largest_num}.')

