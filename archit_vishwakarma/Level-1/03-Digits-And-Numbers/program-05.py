n = input("Enter a number : ")

try:
    n = int(n)
    if n < 1000 and n > 99:
        
        a = n%10
        b = (n//10)%10
        c = (n//100)%10

        print(f"Total of digits in number : {a+b+c}")
        
    else:
        print("Enter a Three Digit Number")
except ValueError:
    print("enter a valid number")