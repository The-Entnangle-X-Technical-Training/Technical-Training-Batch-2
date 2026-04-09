n = input("Enter a number : ")

try:
    n = int(n)
    print(f"Last digit : {n%10}")
except ValueError:
    print("enter a valid number")