n = input("\nEnter a number : ")

try:
    n = int(n)
    if n < 1000 and n > 99:

        a = n//100
        b = (n//10)%10
        c = n%10

        print(f"Product of all digit : {a*b*c}\n")

    else:
        print("Enter a THREE Digit Number")
except ValueError:
    print("enter a valid number")