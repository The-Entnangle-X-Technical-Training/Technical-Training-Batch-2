num=int(input("Enter number to reverse:"))
count=0
while(num>0):
    nu=num%10
    count=(count*10)+nu
    num//=10
print("The reverse Number is:-",count)