# Product of All Digits
# Write a program that takes a 3-digit number as input and calculates the product of all its digits, then displays the result.

num = int(input('Enter a 3-digit number: '))    # 456

last_digit = num % 10           # 6
mid_digit = (num // 10) % 10    # 5
first_digit = num // 100        # 4

product = first_digit * mid_digit * last_digit

print(f'The product of digits {first_digit}, {mid_digit}, and {last_digit} is: {product}')