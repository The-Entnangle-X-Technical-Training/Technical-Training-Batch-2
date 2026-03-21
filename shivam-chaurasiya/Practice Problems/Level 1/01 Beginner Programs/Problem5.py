# Swap Two Numbers Using Third Variable
# Write a program that takes two numbers as input, swaps them using a third temporary variable, and displays values before and after swapping.

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

print(f'Before Swapping num1 and num2 is {num1} and {num2}')

temp = num1
num1 = num2
num2 = temp

print(f'After Swapping num1 and num2 is {num1} and {num2}')