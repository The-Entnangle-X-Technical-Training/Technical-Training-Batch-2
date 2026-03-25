num=int(input("Enter number to give sum of Divisior :"))
sum=0
for i in range(1,num):
        if(num%i==0 ):
            print(i,"+",end="")
            sum+=i
print("=Sum of all Factor:",sum)
        