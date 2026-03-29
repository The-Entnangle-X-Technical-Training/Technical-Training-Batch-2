# Sum of Divisors
# Write a program that takes a number N and calculates the sum of all its divisors (excluding N itself).
# Example: Divisors of 12 are 1, 2, 3, 4, 6, so sum = 16

num = int(input('Enter a number: ')) 
divisors_sum = 0

for i in range(1, num):
    if num % i == 0:
        divisors_sum+=i
print(f'The sum of divisors of {num} (excluding {num}) is: {divisors_sum}')