num=int(input("Enter number to print Nth prime number:"))
for i in range(2,num):
    count=0
    for j in range(2,i):
        if(i%j==0 ):
            count=1
            break
    if count==0:
        print(i)
        