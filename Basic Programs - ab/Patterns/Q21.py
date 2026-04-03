#Problem 21: Square with Row Numbers
#Write a program that prints N×N square where each row shows its row number.
rows=int(input("Enter the number of rows: "))
for i in range(1,rows+1):
    for j in range(1,rows+1):
        print(i,end=' ')
    print()