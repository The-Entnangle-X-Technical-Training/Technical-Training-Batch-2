# Check Divisibility by 3 Using Digit Sum
# Write a program that takes a number as input, calculates the sum of its digits, and checks if the number is divisible by 3 using the digit sum rule.

num = int(input('Enter a number: '))
n = num
digit_sum = 0
while num > 0:
    r = num % 10
    digit_sum = digit_sum + r
    num = num // 10
    
if digit_sum%3==0:
    print(f"The Sum of digits of {n} is {digit_sum}, which is divisible by 3.")
else:
    print(f"The Sum of digits of {n} is {digit_sum}, which is not divisible by 3.")