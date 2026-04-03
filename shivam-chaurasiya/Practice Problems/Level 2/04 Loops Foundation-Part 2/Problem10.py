# Arithmetic Progression - Sum of Series
# Write a program that calculates the sum of first N terms of an AP using a loop.

a = int(input('Enter a first term (a): '))          # 5
d = int(input('Enter a common difference (d): '))   # 3
n = int(input('Enter a number of terms (N): '))     # 4
    
total_sum = 0
for _ in range(n):
    print(a, end=' ')
    total_sum += a
    a = a + d
print(f'\nThe sum of first {n} terms is: {total_sum}.')