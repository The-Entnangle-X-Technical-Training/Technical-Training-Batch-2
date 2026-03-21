# Smallest of Two Numbers
# Write a program that takes two numbers as input and displays which one is smaller.


num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if num1 < num2:
    print(f'{num1} is smaller than {num2}')
elif num2 < num1:
    print(f'{num2} is smaller than {num1}')
else:
    print(f'Both numbers are equal {num1} = {num2}')
