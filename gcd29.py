a=int(input("Enter number to give gcd method :"))
b=int(input("Enter number to give gcd method :"))
if(a>b):
 while(b>0):
    c=a%b
    if(c==0):
        print(b)
    a=b
    b=c