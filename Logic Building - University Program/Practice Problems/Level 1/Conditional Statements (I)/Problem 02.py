#Problem 02: Positive or Negative
Number = int(input("Enter a number: "))

if Number%2 == 0:
    print(Number, "is an even number")
elif Number%2 != 0:
    print(Number, "is an odd number")
else:
    print("Invalid number")