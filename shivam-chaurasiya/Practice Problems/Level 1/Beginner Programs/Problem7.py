# Simple Interest Calculator
# Write a program that calculates simple interest using the formula: SI = (P × R × T) / 100, where P is principal, R is rate, and T is time.

principal = float(input('Enter the principal: '))
rate = float(input('Enter the Rate: '))
time = float(input('Enter the time: '))

simple_interest = (principal * rate * time) / 100

print(f'Simple interest is: {simple_interest}')