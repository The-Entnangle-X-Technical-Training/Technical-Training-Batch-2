# Harshad/Niven Number Checker (3-digit)
# Write a program that takes a 3-digit number, calculates the sum of its digits, and checks if the number is divisible by this sum. Example: 153 → 1+5+3=9, 153÷9=17 → Harshad Number. Display "Harshad Number" or "Not Harshad Number".

num  = int(input('Enter a 3-digit number: '))

last_digit = num % 10
middle_digit = (num // 10) % 10
first_digit = num // 100

digit_sum = first_digit + middle_digit + last_digit

if num % digit_sum == 0:
    print("Harshad Number")
else:
    print("Not Harshad Number")

