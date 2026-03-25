num=int(input("Enter number to give sum of Divisior :"))
perfect=num
sum=0
for i in range(1,num):
        if(num%i==0 ):
            sum+=i
if(perfect==sum):
    print("This is Perfect Number:")
else:
     print(sum)
     print("This is NOT Perfect Number:")
        