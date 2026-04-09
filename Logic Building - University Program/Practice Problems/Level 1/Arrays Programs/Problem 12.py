

Array = []
for i in range(5):
    num = int(input(f"Enter Number {i+1}: "))
    Array.append(num)

X = int(input("Enter the number you want to find: "))
if X in Array:
    print("Found")
else:
    print("Not Found")