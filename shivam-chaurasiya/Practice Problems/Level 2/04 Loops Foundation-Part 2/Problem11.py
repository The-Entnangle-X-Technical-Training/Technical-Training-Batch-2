# Sum of Series: 1 + 1/2 + 1/3 + ... + 1/N
# Write a program that calculates the sum of the harmonic series up to N terms.

n = int(input('Enter a number: '))

total_sum = 0

for i in range(1, n+1):
    total_sum += 1 / i
print(f'{total_sum:.2f}')