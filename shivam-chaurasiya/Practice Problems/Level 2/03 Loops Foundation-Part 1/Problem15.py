# Reverse a Number using Loop
# Write a program that takes a number and prints it in reverse using a loop.
# Hint: Extract digits one by one and build reversed number


num = int(input('Enter a number: ')) # 123
n = num
reversed_number = 0

while num > 0:
    r = num % 10
    reversed_number = (reversed_number * 10) + r
    num = num // 10
print(f'The reverse of {n} is {reversed_number}')
