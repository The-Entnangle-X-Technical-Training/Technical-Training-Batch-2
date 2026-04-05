n = input("Enter a number : ")

try:
    n = int(n)
    for i in range(n+1):
        print("A"*i)
except ValueError:
    print("Enter a valid number")