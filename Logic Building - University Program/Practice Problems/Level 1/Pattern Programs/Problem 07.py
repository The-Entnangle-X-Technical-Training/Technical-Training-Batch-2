#Problem 07: Print N Stars in One Line

N = 4
for row in range(1, N+1):
    for col in range(1, N+1):
        print("*", end=" ")
    print()