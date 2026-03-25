num=int(input("Enter number to count Nth prime number:"))
countt=0
for i in range(2,num):
    count=0
    for j in range(2,i):
        if(i%j==0 ):
            count=1
            break
    if count==0:
        print(i)
        countt+=1
print("Total",countt,"Prime Number:")
        