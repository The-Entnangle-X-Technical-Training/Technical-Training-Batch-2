#Problem 18: Print Numbers 1 to N in Each Row
#Write a program that prints M rows, each containing numbers 1 to N.
rows=int(input("Enter number of rows: "))
size=int(input("Enter the size: "))
for i in range(rows):
    for j in range(1,size+1):
        print(j,end=' ')
    print()