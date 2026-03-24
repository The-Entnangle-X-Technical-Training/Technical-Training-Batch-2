# Palindrome Number Checker (3-digit)
# Write a program that takes a 3-digit number as input and checks if it is a palindrome. Example: 121 → Yes, 123 → No. Display "Palindrome" or "Not Palindrome".

num = int(input('Enter a 3-digit number: '))    # 121

last_digit = num % 10

first_digit = num // 100

if first_digit == last_digit:
    print('Palindrome')
else:
    print('Not Palindrome')