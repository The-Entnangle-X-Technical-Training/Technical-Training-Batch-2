#Problem 05: Find Maximum Element

Array = []
for i in range(5):
    num = int(input(f"Enter Number {i+1}: "))
    Array.append(num)

Maximum = max(Array)
print(f"Maximum Array Element: {Maximum}")