# Print Stars Equal to Row Number
# Write a program that prints row number of stars in each row for N rows.
# *
# * *
# * * *
# * * * *
# * * * * *

n = int(input('Enter a rows: '))    # 5

# First Method
for i in range(n):
    for _ in range(i+1):
        print("*", end=" ")
    print()
    
# Second Method
# for i in range(1, n + 1):
#     print("* " * i)   
