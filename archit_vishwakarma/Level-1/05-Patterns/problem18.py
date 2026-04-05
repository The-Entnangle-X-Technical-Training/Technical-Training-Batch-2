n = input("Enter a number : ")
m = input("Enter number of rows : ")
try:
    n = int(n)
    m = int(m)
    for i in range(1, m+1):
        for j in range(1, n+1):
            print(j, end=" ")
        print("")
except ValueError:
    print("Enter a valid number")