#Problem 11: Continuous Number Pattern

N = 4
count = 1
for row in range(1, N+1):
    for col in range(1,row+1):
        print(count, end=" ")
        count = count+1
    print()
    