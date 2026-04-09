#Problem 07: Display Array in Reverse

Array = []
for i in range(5):
    num = int(input(f"Enter Number {i+1}: "))
    Array.append(num)
print(f"Array After Reversed: {Array[::-1]}")