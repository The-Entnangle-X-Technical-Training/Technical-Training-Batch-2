num=int(input("Enter number to give Fibbonacci Series :"))
j=1
k=0
for i in range(0,num-1):
    if(i==0):
        print(k,end=" ")
        print(j,end=" ")
    else:
        sum=k+j
        print(sum,end=" ")
        k=j
        j=sum 
        sum=0