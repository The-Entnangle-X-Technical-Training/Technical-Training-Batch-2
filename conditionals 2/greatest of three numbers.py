a=int(input("Enter a Number :"))
b=int(input("Enter a Number :"))
c=int(input("Enter a Number :"))
if(a>=b and a>=c):
    print("Greatest Number is ",a)
elif(b>=a and b>=c):
    print("Greatest numbers is :",b)
else:
    print("Greatest Number is",c)