#Problem 11: Sum of Odd Numbers

Array = []
odd = []
for i in range(5):
    num = int(input(f"Enter Number {i+1}: "))
    Array.append(num)
for num in Array:
    if num % 2 != 0:
        odd.append(num)
total = sum(odd)
print(f"Sum of all odd numbers: {total}")
  