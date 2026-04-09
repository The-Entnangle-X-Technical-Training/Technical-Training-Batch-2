#Problem 15: Average of Array Elements

Array = []
for i in range(5):
    num = int(input(f"Enter Number {i+1}: "))
    Array.append(num)

total = sum(Array)
Average = total/len(Array)
print(f"Average of Array Elements: {Average}")