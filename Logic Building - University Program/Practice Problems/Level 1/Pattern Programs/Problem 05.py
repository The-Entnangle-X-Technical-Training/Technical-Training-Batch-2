#Problem 05: Right Triangle - Same Number Each Row

N = 4
for row in range(1, N+1):
    for col in range(1, row+1):
        print(row, end=" ")
    print()