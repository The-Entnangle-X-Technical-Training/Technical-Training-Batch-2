# Extract Middle Digit of 3-Digit Number
# Write a program that takes a 3-digit number as input and extracts and displays the middle digit.


num = int(input('Enter a 3-digit number: '))  # 432

middle_digit = (num // 10) % 10

print(f'Middle Digit is: {middle_digit}')