#Problem 06: Find Minimum Element

Array = []
for i in range(5):
    num = int(input(f"Enter Number {i+1}: "))
    Array.append(num)

Minimum = min(Array)
print(f"Maximum Array Element: {Minimum}")