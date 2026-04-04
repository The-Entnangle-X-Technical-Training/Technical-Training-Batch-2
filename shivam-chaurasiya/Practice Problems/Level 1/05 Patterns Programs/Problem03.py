# Right Triangle - Stars (Increasing)
# Write a program that prints this star pattern for N rows.
# *
# * *
# * * *
# * * * *

r = int(input('Enter a rows: '))

for i in range(r):
    for _ in range(i+1):
        print("*", end=' ')
    print()
