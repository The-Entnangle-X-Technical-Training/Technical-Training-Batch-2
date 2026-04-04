# Rectangle Pattern (M×N)
# Write a program that takes M (rows) and N (columns) and prints a rectangle pattern.

m = int(input('Enter a rows: '))        # 3
n = int(input('Enter a columns: '))     # 4

for _ in range(m):
    for _ in range(n):
        print("*", end=' ')
    print()

