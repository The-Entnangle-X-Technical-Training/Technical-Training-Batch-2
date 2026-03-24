# Greater of Two Numbers
# Write a program that takes two numbers as input and displays which one is greater.

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

if num1 > num2:
    print(f'{num1} is a greater than {num2}')
elif num1 < num2:
    print(f'{num1} is a less than {num2}')
else:
    print(f'{num1} is equal to {num2}')