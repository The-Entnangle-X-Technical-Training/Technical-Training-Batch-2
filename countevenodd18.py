num=int(input("Enter number to count even/odd digit:"))
count=0
countt=0
while(num>0):
    nu=num%10
    if(nu%2==0):
        count+=1
    else:
        countt+=1
    num//=10
print("The Even digit is-",count)
print("The Odd Digit is-",countt)