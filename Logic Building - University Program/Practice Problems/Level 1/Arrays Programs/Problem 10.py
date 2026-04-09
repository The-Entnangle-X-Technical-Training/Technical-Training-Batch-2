#Problem 10: Sum of Even Numbers

Array = []
even = []
for i in range(5):
    num = int(input(f"Enter Number {i+1}: "))
    Array.append(num)
for num in Array:
    if num % 2 == 0:
        even.append(num)
total = sum(even)
print(f"Sum of all even numbers: {total}")
  