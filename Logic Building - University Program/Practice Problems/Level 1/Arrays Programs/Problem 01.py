#Problem 01: Input and Display Array

Array = []
for i in range(5):
    num = int(input(f"Enter Number {i + 1}: "))
    Array.append(num)
print("The Numbers are: ", Array)