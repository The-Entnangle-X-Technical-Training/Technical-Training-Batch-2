#Problem 03: Right Triangle - Stars (Increasing)
N = 5
for row in range(1, N+1):
    for col in range(0, row):
        print("*", end=" ")
    print()