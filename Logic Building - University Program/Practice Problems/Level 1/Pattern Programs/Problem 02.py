#Problem 02: Rectangle pattern (M*N)

m = 3
n = 5

for row in range(1, m+1):
    for col in range(1, n+1):
        print("*", end=" ")
    print()