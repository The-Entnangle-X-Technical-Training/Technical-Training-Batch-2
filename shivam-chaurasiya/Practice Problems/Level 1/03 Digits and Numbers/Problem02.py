# Remove Last Digit
# Write a program that takes a number as input and displays the number after removing its last digit.


num = int(input('Enter a number :'))

delete_last_digit = num // 10
print(f'After removing last digit: {delete_last_digit}')
