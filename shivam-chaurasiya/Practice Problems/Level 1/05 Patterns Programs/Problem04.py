# Right Triangle - Numbers (Rows)
# Write a program that prints this number pattern for N rows.
# 1
# 1 2
# 1 2 3
# 1 2 3 4

n = int(input('Enter a rows: '))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()