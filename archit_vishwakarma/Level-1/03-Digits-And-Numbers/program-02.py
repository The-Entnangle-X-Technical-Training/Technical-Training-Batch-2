n = input("Enter a number : ")

try:
    n = int(n)
    print(f"after removing last digit : {n//10}")
except ValueError:
    print("enter a valid number")