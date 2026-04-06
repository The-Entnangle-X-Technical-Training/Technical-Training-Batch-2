# Print Numbers 1 to N in Each Row
# Write a program that prints M rows, each containing numbers 1 to N.
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

m = int(input('Enter a rows: '))
n = int(input('Enter a numbers: '))

for _ in range(m):
    for j in range(1, n+1):
        print(j, end=' ')
    print()