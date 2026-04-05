n = input("Enter a number : ")

try:
    n = int(n)
    for i in range(n, 0, -1):
        print("*"*i)
except ValueError:
    print("Enter a valid number")