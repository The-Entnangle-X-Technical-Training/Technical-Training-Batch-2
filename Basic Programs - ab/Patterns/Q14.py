#Print Multiplication Table in Grid
#Write a program that prints 4×4 multiplication table grid.
size=int(input("Enter the size: "))
for i in range(1,size+1):
    for j in range(1,size+1):
        print(i*j,end=' ')
    print()