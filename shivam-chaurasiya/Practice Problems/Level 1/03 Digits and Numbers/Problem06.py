# Reverse a 2-Digit Number
# Write a program that takes a 2-digit number as input and displays it in reverse order (e.g., 45 becomes 54).

num = int(input('Enter a 2-digit number: '))    # 34

first_digit = num // 10 # 3

last_digit = num % 10   # 4

print(f'Reveresed number is: {last_digit}{first_digit}')

