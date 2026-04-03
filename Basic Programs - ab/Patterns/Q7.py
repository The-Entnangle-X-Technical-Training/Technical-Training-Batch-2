#Problem 7: Print N Rows of N Stars
rows=int(input("Enter the number of rows : "))
size=int(input("Enter the number of stars you want to print: "))
for i in range(rows):
    for j in range(size):
        print("*",end=' ')
    print()