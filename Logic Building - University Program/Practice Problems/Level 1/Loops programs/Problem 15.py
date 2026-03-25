#Problem 15: Count Odd Numbers from 1 to N
N = int(input("Enter number N: "))
count = 0
for i in range(1,N+1):
    if i %2 != 0:
        print(i, end=" ")
        count = count +1 
print("\nOdd number count from 1 to", N,":", count)