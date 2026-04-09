n = input("\nEnter a number : ")

try:
    n = int(n)
    if n < 10000 and n > 999:

        a = n//1000
        b = n%10
        
        print(f"Average of first and last digit : {(a+b)/2}\n")

    else:
        print("Enter a FOUR Digit Number")
except ValueError:
    print("enter a valid number")


