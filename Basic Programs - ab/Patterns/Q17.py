#Problem 17: Square Border Pattern
#Write a program that prints hollow square (only borders) for N×N size.
size=int(input("Enter the size: "))
for i in range(size):
    for j in range(size):
        if(i==0 or i==size-1 or j==0 or j==size-1):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()