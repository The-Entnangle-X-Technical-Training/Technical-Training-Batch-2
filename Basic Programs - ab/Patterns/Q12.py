#Problem 12: Reverse Numbers Pattern
#Write a program that prints reverse numbers in each row for N rows.
size=int(input("Enter the size: "))
for i in range(1,size+1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()