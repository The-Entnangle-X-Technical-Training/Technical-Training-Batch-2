# Print 1 to N, N Times
# Write a program that prints numbers 1 to N in each row, for N rows.
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

n = int(input('Enter a rows: '))    # 4

for _ in range(1, n+1):
    for j in range(1, n+1):
        print(j, end=" ")
    print()