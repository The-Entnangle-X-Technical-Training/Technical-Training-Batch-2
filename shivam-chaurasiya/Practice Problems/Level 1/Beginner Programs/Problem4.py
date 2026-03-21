# Sum and Average of Three Numbers
# Write a program that takes three numbers as input and calculates their sum and average, then displays both results.

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))

sum = num1 + num2 + num3
average = sum/3

print(f'The Sum of {num1}, {num2} and {num3} is: {sum}')
print(f'The Average of {num1}, {num2} and {num3} is: {average}')