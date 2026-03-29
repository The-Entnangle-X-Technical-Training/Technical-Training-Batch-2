# Sum of First N Odd Numbers
# Write a program that takes a number N and calculates the sum of first N odd numbers.

num = int(input('Enter a number N: '))
odd_sum = 0

for i in range(1, num * 2, 2):
    odd_sum+=i 
    
print(f'The sum of first {num} Odd Numbers is: {odd_sum}.')