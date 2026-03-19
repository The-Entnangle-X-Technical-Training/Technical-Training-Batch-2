#Problem 15: Swap Two Numbers Without Third Variable

First_Number = int(input("Enter the first number: "))
Second_Number = int(input("Enter the second number: "))

print("Number before swapping - ")
print("First number: ", First_Number)
print("Second number: ", Second_Number)

First_Number, Second_Number = Second_Number, First_Number

print("Numbers after swapping - ")
print("First number: ", First_Number)
print("Second number: ", Second_Number)