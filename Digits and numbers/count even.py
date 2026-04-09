num=int(input("Enter a 4 digit number :"))
c1=num//1000
c2=(num//100)%10
c3=(num//10)%10
c4=num%10

count=0
if(c1%2==0):
    count+=1
if(c2%2==0):
    count+=1
if(c3%2==0):
    count+=1
if(c4%2==0):
    count+=1

print("Number of Even Digits :",count)