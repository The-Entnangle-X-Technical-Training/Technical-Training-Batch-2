# Alphabet Pattern (Single Letter)
# Write a program that prints letter A in triangle pattern for N rows.
# A
# A A
# A A A
# A A A A

n = int(input('Enter a rows: '))    # 4

for i in range(1, n+1):
    for _ in range(1, i+1):
        print('A', end=' ')     
    print()