# Sum of Series: 1 - 2 + 3 - 4 + 5 - 6 + ... ± N
# Write a program that calculates this alternating series.

n = int(input('Enter a number: '))

total_sum = 0

for i in range(1, n+1):
    if i % 2 != 0:
        total_sum += i
    else:
        total_sum -= i
print(f'The sum of series is: {total_sum}')
