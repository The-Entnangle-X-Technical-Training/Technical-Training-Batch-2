# Find Smallest Digit in a Number
# Write a program that takes a 4-digit number as input and finds the smallest digit in it, then displays that digit.

num = int(input('Enter a 4-digit number: '))    # 4567
n = num

r1 = num % 10       # 7
num = num // 10     # 456
r2 = num % 10       # 6
num = num // 10     # 45
r3 = num % 10       # 5
num = num // 10     # 4
r4 = num % 10       # 4

if r1 <= r2 and r1 <= r3 and r1 <= r4:
    print(f'{r1} is the smallest digit in {n}')
elif r2 <= r1 and r2 <= r3 and r2 <= r4:
    print(f'{r2} is the smallest digit in {n}')
elif r3 <= r1 and r3 <= r2 and r3 <= r4:
    print(f'{r3} is the smallest digit in {n}')
else:
    print(f'{r4} is the smallest digit in {n}')