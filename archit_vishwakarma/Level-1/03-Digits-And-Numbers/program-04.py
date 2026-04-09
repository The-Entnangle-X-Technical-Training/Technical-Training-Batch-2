n = input("Enter a number : ")

try:
    n = int(n)
    if n < 1000 and n > 99:
        last_2 = n%100
        mid = last_2//10
        print(f"middle digit : {mid}")
    else:
        print("Enter a Three Digit Number")
except ValueError:
    print("enter a valid number")