# Plus Sign Pattern
# Write a program that prints a plus (+) sign pattern using stars.
#     *
#     *
# * * * * *
#     *
#     *

n = int(input('Enter a number: '))

for i in range(n):
    for j in range(n):
        if i == (n//2) or j == (n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    