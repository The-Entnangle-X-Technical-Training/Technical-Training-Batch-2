# Print Multiplication Table in Grid
# Write a program that prints 4×4 multiplication table grid.
# 1 2 3 4
# 2 4 6 8
# 3 6 9 12
# 4 8 12 16

n = int(input('Enter a rows: '))    # 4

for i in range(1, n+1):
    for j in range(1, n+1):
        print(i * j, end=' ')     
    print()