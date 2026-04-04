# Inverted Right Triangle - Stars
# Write a program that prints this inverted pattern for N rows.
# * * * *
# * * *
# * *
# *

n = int(input('Enter a rows: '))    # 4

for i in range(n):
    for _ in range(n-i):
        print("*", end=" ")
    print()