# Count Multiples
# Write a program that takes two numbers N and M. Count how many multiples of M exist from 1 to N. Example: If N=20 and M=3, multiples are 3, 6, 9, 12, 15, 18, so count = 6

n = int(input('Enter first number N: '))
m = int(input('Enter second number M: '))

count = 0 

for i in range(1, n+1):
    if i % m == 0:
        count+=1
print(f'{count} multiples of {m} exist from 1 to {n}')
        