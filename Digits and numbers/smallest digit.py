num=int(input("Enter a 4 digit number :"))
s1=num//1000
s2=(num//100)%10
s3=(num//10)%10
s4=num%10

print(s1)
print(s2)
print(s3)
print(s4)

smallest=s1
if(s2<smallest):
    smallest=s2
if(s3<smallest):
    smallest=s3
if(s4<smallest):
    smallest=s4
print("Smallest Number :",smallest)