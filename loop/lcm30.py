a=int(input("Enter number to give gcd method :"))
b=int(input("Enter number to give gcd method :"))
c1=a*b
if(a>b):
 while(b>0):
    c=a%b
    if(c==0):
        lcm=c1//b
        print(b)
        print(lcm)
    a=b
    b=c