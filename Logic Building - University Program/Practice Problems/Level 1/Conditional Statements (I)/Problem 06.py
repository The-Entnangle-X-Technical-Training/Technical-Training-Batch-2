#Problem 06: Check if Number is Positive

Number = int(input("Enter the number: "))

if Number > 0:
    print(Number, "is a positive number")
elif Number < 0:
    print(Number, "is a negative number")
else:
    print("Number is zero")
    