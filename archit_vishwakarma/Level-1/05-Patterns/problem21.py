n = input("Enter a number : ")

try:
    n = int(n)
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i, end="")
        print("")
except ValueError:
    print("Enter a valid number")