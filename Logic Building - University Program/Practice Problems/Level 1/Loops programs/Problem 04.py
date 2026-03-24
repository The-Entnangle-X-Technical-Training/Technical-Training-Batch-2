#Problem 04: Print first 10 even numbers
num = 50
count = 0
for i in range(0,num+1):
    if i %2 == 0:
        print(i, end=' ')
        count = count +1 
        if count == 10:
            break
