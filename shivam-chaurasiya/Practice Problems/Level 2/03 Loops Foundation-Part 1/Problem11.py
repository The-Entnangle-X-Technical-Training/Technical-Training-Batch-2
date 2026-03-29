#  Power Calculator
# Write a program that takes two numbers base and exponent, and calculates base^exponent using a loop (without using pow function)

base = int(input('Enter a first number: '))
exponent = int(input('Enter a second number: '))

for b in range(base, exponent):
    print(b ** exponent)
    break
