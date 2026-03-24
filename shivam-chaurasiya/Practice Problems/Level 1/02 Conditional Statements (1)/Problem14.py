# Smallest of Three Numbers
# Write a program that takes three numbers as input and displays the smallest among them.

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))


if num1 == num2 == num3:
    print("All three numbers are equal.")
elif (num1 <= num2) and (num1 <= num3):
    print(f'{num1} is smallest than {num2} and {num3}')
elif (num2 <= num1) and (num2 <= num3):
    print(f'{num2} is smallest than {num1} and {num3}')
else:
    print(f'{num3} is smallest than {num1} and {num2}')