# Print First N Even Numbers
# Write a program that takes a number N and prints the first N even numbers (e.g., N=4, then first N even numbers (2, 4, 6, 8)).

num = int(input('Enter a number N: '))

print(f'The first {num} even numbers are: ')
for i in range(2, (num * 2) + 1):
    if i % 2 == 0:
        print(i, end=' ')