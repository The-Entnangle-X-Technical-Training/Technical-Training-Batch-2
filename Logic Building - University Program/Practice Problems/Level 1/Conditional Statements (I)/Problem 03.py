#Problem 03: Greater of Two number

First_Number = int(input("Enter the first number: "))
Second_Number = int(input("Enter the second number: "))

if First_Number > Second_Number:
    print(First_Number, "is greater than", Second_Number, "(first number is greater)")
elif First_Number < Second_Number:
    print(Second_Number, "is greater than", First_Number, "(second number is greater)")
elif First_Number == Second_Number:
    print(First_Number, "=", Second_Number, "(both numbers are equal)")
else:
    print("Invalid number")