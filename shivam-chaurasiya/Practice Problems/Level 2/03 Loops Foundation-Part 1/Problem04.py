# Print First N Odd Numbers
# Write a program that takes a number N=5 and prints the first N odd numbers (e.g., N=5, then first N odd numbers (1, 3, 5, 7, 9)).

num = int(input('Enter a number N: '))

print(f'The first {num} odd numbers are: ')
for i in range(1, (num * 2)):
    if i % 2 != 0:
        print(i, end=' ')