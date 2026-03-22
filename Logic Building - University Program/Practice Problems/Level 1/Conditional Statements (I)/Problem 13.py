#Problem 13: Greatest of Three Numbers

First_Number = int(input("Enter first number: "))
Second_Number = int(input("Enter second number: "))
Third_Number = int(input("Enter third number: "))

if First_Number > Second_Number and First_Number > Third_Number:
    print("First number is the greatest.")
elif Second_Number > First_Number and Second_Number > Third_Number:
    print("Second number is the greatest.")
else:
    print("Third number is the greatest.")
