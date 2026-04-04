# Print N Stars in One Line
# Write a program that takes N and prints N stars in a single line.
# * * * * *

n = int(input('Enter a rows: '))

for _ in range(n):
    print('*', end=' ')