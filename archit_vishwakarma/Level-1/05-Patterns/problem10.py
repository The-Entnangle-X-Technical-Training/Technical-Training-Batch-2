n = input("Enter a number : ")

try:
    n = int(n)
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(j, end="")
        print("")
except ValueError:
    print("Enter a valid number")