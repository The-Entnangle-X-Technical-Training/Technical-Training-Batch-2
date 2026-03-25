#Problem 05: Print First 10 Odd number

num = 50
count = 0
for i in range(1,num+1):
    if i %2 != 0:
        print(i, end=' ')
        count = count +1 
        if count == 10:
            break
