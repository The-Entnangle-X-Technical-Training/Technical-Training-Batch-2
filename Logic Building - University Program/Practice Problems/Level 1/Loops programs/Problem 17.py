#Problem 17: Sum of Odd Numbers (1 to N)

N = int(input("Enter number N: "))
sum = 0
for i in range(1,N+1):
    if i %2 != 0:
        sum += i
        print(sum, end=" ")