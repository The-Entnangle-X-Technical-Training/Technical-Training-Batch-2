N = 4
for row in range(1, N+1):
    for col in range(row, 0, -1):
        print(col, end=" ")    
    print()