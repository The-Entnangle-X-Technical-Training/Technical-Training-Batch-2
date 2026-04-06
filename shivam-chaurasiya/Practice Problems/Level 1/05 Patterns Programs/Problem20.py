# Right Triangle - Increasing Stars
# Write a program that prints stars without spaces (continuous) for N rows.
# *
# **
# ***
# ****

n = int(input('Enter a rows: '))    # 4

for i in range(n):
    for _ in range(i+1):
        print("*", end="")
    print()