#Problem 20: Right Triangle - Increasing Stars
#Write a program that prints stars without spaces (continuous) for N rows.
rows=int(input("Enter the number of rows: "))
for i in range(1,rows+1):
    for j in range(i):
        print("*",end='')
    print()