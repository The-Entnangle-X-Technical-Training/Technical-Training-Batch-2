num=int(input("Enter number to chek Strong Number:"))
strng=num
multiple=1
multi=0
while(num>0):
    nu=num%10
    for i in range(1,nu+1):
        multiple*=i
    multi+=multiple
    num=num//10
    multiple=1
if(multi==strng):
    print("This is Strong number")
else:
    print("This is NOT Strong number")