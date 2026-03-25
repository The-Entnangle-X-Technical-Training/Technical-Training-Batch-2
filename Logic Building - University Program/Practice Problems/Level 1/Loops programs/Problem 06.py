#Problem 06: Print first N Even Numbers

N = int(input("Enter N: "))
for i in range(1,N+1):
    if i %2 == 0:
        print(i, end=' ')
        
        