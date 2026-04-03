#Problem 24: Simple Diagonal Pattern
#Write a program that prints stars diagonally for N rows.
rows=int(input("Enter the number of rows: "))
for i in range(1,rows+1):
    for j in range(rows+1):
        if(j==i):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()   