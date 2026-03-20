#Problem 10: Smallest of Two Numbers

First_Number = int(input("Enter the first number: "))
Second_Number = int(input("Enter the second number: "))

if First_Number < Second_Number:
    print(First_Number, "is smaller than", Second_Number, "(first number is smaller)")
elif First_Number > Second_Number:
    print(Second_Number, "is smaller than", First_Number, "(second number is smaller)")
elif First_Number == Second_Number:
    print(First_Number, "=", Second_Number, "(both numbers are equal)")
else:
    print("The number is invalid")