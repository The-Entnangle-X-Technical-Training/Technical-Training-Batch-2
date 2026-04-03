#Problem 25: Plus Sign Pattern
#Write a program that prints a plus (+) sign pattern using stars.
n = int(input("Enter size (odd number): "))
mid = n // 2
for i in range(n):
    for j in range(n):
        if i == mid or j == mid:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()