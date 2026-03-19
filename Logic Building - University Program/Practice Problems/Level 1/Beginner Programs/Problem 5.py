#Problem 5: Swap Two Numbers using a Third Variable

First_Number = int(input("Enter the first number: "))
Second_Number = int(input("Enter the Second number: "))

print("Variables before swapping - ")
print("first Variable: ", First_Number)
print("Second Variable: ", Second_Number)

Temporary_Variable = First_Number
First_Number = Second_Number
Second_Number = Temporary_Variable

print("Variables after swapping - ")
print("first Variable: ", First_Number)
print("Second Variable: ", Second_Number)