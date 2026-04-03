#Problem 10: Print 1 to N, N Times
#Write a program that prints numbers 1 to N in each row, for N rows.
size=int(input("Enter the number of size: "))
for i in range(size):
    for j in range(1,size+1):
        print(j,end=' ')
    print()