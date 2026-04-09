n = input("Enter a number : ")

try:
    n = int(n)
    if n < 100 and n > 9:
        
        a = n%10
        b = a*10
        reverse = b + (n//10)

        print(f"reverse of two digit : {reverse}")
        
    else:
        print("Enter a Two Digit Number")
except ValueError:
    print("enter a valid number")