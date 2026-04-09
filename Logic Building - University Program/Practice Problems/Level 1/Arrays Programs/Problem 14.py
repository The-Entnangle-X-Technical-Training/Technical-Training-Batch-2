#Problem 14: Count Negative Numbers

Array = []
count = 0
for i in range(5):
    num = int(input(f"Enter Number {i+1}: "))
    Array.append(num)
for num in Array:
    if num < 0:
        count = count + 1
print(f"Total Negative numbers: {count}")