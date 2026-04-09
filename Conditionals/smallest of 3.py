a=int(input("Enter a number :"))
b=int(input("Enter a number :"))
c=int(input("Enter a number :"))
if(a<=b) and (a<=c):
    smallestest=a
elif(b<=a) and (b<=c):
    smallest=b
else:
    smallest=c
print("The Smallest number is :", smallest)