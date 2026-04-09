

Array = []
for i in range(5):
    num = int(input(f"Enter Number {i + 1}: "))
    Array.append(num)
for i in range(len(Array)):
    print(f"The number on index {i} is {Array[i]}")