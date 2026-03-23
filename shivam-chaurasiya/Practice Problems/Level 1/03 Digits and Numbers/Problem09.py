# Average of First and Last Digit
# Write a program that takes a 4-digit number and calculates the average of its first and last digits (e.g.,  4567 = (4 + 7)/2 = 5.5).

num = int(input('Enter a 4-digit number: '))    # 4567

first_digit = num // 1000
last_digit = num % 10

first_last_digit_average = (first_digit + last_digit) / 2

print(f'The Average of first {first_digit} and last {last_digit} digits is: {first_last_digit_average}')