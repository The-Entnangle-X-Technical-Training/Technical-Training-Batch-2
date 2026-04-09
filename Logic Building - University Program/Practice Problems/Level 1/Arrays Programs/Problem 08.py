#Problem 08: Count Even Numbers

Array = []
Even_count = 0
for i in range(5):
    num = int(input(f"Enter Number {i+1}: "))
    Array.append(num)

for num in Array:
    if num % 2 == 0:
        Even_count = Even_count+1
print(f"Number of Even Elements: {Even_count}")