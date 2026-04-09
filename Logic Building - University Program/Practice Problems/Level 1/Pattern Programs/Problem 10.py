#Problem 10: Print 1 to N, N Times

N = 4
for row in range(1, N+1):
    for col in range(1, N+1):
        print(col, end=" ")
    print()