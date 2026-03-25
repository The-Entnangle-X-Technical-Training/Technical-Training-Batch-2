num=int(input("Enter number to chek Prime Number:"))
isPrime=0
n=1
for i in range(2,num):
    if(num%i==0):
        isPrime=1
        break
if(isPrime==0):
    print("This is Prime Number")
else:
     print("This is NOT Prime Numer")