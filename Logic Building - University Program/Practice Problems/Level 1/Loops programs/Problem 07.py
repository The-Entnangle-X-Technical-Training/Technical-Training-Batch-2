#Problem 07: Print first N Odd Numbers

N = int(input("Enter N: "))
for i in range(1,N+1):
    if i %2 != 0:
        print(i, end=' ')