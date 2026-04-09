#Problem 04: Count Elements in Array

Array = []
for i in range(5):
    num = int(input(f"Enter Number {i+1}: "))
    Array.append(num)

count = len(Array)
print(f"Length of Array Elements: {count}")