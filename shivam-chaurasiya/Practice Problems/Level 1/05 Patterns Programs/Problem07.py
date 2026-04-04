# Print N Rows of N Stars
# Write a program that prints N rows, each having N stars.
# * * * *
# * * * *
# * * * *
# * * * *

n = int(input('Enter a rows: '))

for _ in range(n):
    for _ in range(n):
        print('*', end=' ')
    print()