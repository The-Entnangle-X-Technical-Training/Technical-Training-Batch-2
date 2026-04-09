n = input("\nEnter a number : ")

try:
    n = int(n)
    if n < 1000 and n > 99:

        a = ((n%10)*100) + (n%100)
        b = ((a//10)*10) + (n//100)
        
        print(f"after swaping first and last digit : {b}\n")

    else:
        print("Enter a Three Digit Number")
except ValueError:
    print("enter a valid number")


