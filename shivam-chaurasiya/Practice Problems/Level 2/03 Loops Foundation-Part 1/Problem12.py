# Sum of Series: 1² + 2² + 3² + ... + N²
# Write a program that takes N and calculates the sum: 1² + 2² + 3² + ... + N²

n = int(input('Enter a number N: '))
digit_sum = 0

for i in range(1, n+1):
    digit_sum += i ** 2
    
print(f'The Sum of Power 1 to {n} is: {digit_sum}')