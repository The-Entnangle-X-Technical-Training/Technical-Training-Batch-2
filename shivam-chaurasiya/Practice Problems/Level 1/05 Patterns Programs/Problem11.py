# Continuous Number Pattern
# Write a program that prints continuous numbers in triangle pattern for N rows.
# 1
# 2 3
# 4 5 6
# 7 8 9 10

n = int(input('Enter a rows: '))    # 4
num = 1

for i in range(1, n+1):
    for _ in range(1, i+1):
        print(i, end=' ')
        i += 1
    print()