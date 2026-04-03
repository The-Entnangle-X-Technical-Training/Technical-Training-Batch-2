#Problem 23: Print Stars Equal to Row Number
#Write a program that prints row number of stars in each row for N rows.
rows=int(input("Enter the number of rows: "))
for i in range(1,rows+1):
    for j in range(i):
        print("*",end=' ')
    print()