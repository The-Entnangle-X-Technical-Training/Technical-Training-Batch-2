# Sum of First N Natural Numbers
# Write a program that takes a number N and calculates the sum of first N natural numbers (1 + 2 + 3 + ... + N)

n = int(input('Enter first number N: '))
digit_sum = 0

for i in range(1, n+1):
    digit_sum = digit_sum + i
    
print(f'\nThe sum of first {n} natural numbers is: {digit_sum}')
    