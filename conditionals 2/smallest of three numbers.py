a=int(input("Enter a Number :"))
b=int(input("Enter a Number :"))
c=int(input("Enter a Number :"))
if(a<=b and a<=c):
    print("Smallest Number is ",a)
elif(b<=a and b<=c):
    print("Smallest numbers is :",b)
else:
    print("Smallest Number is",c)