# Check if Last Digit is Even
# Write a program that takes any number as input and checks whether its last digit is even or odd, then displays the result.

num = int(input('Enter any number: '))

last_digit = num % 10

if last_digit % 2 == 0:
    print(f'The Last digit {last_digit} of {num} is Even')
else:
    print(f'The Last digit {last_digit} of {num} is Odd')