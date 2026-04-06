# Inverted Numbers Triangle
# Write a program that prints this inverted number pattern for N rows.
# 1 2 3 4
# 1 2 3
# 1 2
# 1

n = int(input('Enter a rows: '))    # 4

for i in range(n):
    for j in range(1, n-i+1):
        print(j, end=" ")
    print()