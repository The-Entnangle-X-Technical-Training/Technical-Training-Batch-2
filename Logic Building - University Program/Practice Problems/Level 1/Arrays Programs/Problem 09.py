#Problem 09: Count Odd Numbers

Array = []
Odd_count = 0
for i in range(5):
    num = int(input(f"Enter Number {i+1}: "))
    Array.append(num)

for num in Array:
    if num % 2 != 0:
        Odd_count = Odd_count+1
print(f"Number of Odd Elements: {Odd_count}")