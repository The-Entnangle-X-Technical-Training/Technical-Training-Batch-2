# Sum of Digits using Loop
# Write a program that takes a number and calculates the sum of its digits using a loop.
# Hint: Extract last digit using %10, add to sum, remove last digit using /10


num = int(input('Enter a number: '))
digit_sum = 0
n = num 

while num > 0:
    r = num % 10 
    digit_sum = digit_sum + r
    num = num // 10
    
print(f'The Sum of {n} is: {digit_sum}')