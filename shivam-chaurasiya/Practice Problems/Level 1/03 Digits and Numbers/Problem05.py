# Sum of Digits (3-digit number)
# Write a program that takes a 3-digit number as input and calculates the sum of all its digits, then displays the result.

num = int(input('Enter a 3-digit number: '))  # 432

last_digit = num % 10

middle_digit = (num // 10) % 10

first_digit = num // 100

digit_sum = first_digit + middle_digit + last_digit

print(f'The sum of {first_digit}, {middle_digit} and {last_digit} is: {digit_sum}')
