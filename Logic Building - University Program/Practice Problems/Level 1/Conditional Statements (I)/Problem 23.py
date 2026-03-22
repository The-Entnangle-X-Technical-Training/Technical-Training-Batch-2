#Problem 23: Check if Number is Divisible by Both 2 and 3

number = int(input("Enter the number: "))

if number % 2 == 0 and number % 3 == 0:
    print("Yes.", number, "is divisible by both 2 and 3.")
else:
    print("No.", number, "is not divisible by both 2 and 3.")