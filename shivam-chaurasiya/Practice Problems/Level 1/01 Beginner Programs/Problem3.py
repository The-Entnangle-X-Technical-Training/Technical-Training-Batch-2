# Simple Calculator
# Write a program that takes two numbers from the user and performs addition, subtraction, multiplication division, and modulus on them, displaying all five results.

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

add = num1 + num2
sub = num1 - num2
multi = num1 * num2
div = num1 / num2
mod = num1 % num2

print(f'The Addition of {num1} and {num2} is: {add}')
print(f'The subtraction of {num1} and {num2} is: {sub}')
print(f'The multiplication of {num1} and {num2} is: {multi}')
print(f'The division of {num1} and {num2} is: {div:.2f}')
print(f'The modulus of {num1} and {num2} is: {mod}')