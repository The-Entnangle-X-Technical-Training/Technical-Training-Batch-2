# Palindrome Number Checker (2-digit)
# Write a program that takes a 2-digit number as input and checks if it is a palindrome (reads same forwards and backwards). Example: 11 → Yes, 23 → No. Display "Palindrome" or "Not Palindrome".

num = int(input('Enter a 2-digit number: '))    # 11 

last_digit = num % 10
first_digit = num // 10

res = (last_digit * 10) + first_digit

if num == res:
    print("Palindrome")
else:
    print("Not Palindrome")