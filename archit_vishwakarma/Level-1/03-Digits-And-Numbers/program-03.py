n = input("Enter a number : ")

try:
    n = int(n)
    if n < 1000 and n > 99:
        print(f"first digit : {n//100}")
    else:
        print("Enter a Three Digit Number")
except ValueError:
    print("enter a valid number")