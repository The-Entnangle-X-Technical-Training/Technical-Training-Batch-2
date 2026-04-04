# Column Pattern - Numbers
# Write a program that prints this pattern for N rows.
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4

n = int(input('Enter a rows: '))    # 4

for i in range(1, n+1):
    for _ in range(n):
        print(i, end=" ")
    print()