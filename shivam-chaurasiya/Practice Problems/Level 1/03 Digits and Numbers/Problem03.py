# Extract First Digit of 3-Digit Number
# Write a program that takes a 3-digit number as input and extracts and displays the first digit.


num = int(input('Enter a 3-digit number: '))  # 432

last_digit = num // 100   # 43

print(f'First Digit is: {last_digit}')
