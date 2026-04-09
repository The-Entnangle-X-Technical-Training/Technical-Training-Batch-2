#Problem 03: Sum of array elements

Array = []
for i in range(5):
    num = int(input(f"Enter Number {i+1}: "))
    Array.append(num)

total = sum(Array)
print(f"sum of Array Elements: {total}")
