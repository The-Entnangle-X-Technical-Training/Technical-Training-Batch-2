num=int(input("Enter number to chek Strong Number:"))
n1=num%10
num=num//10
while(num>0):
    n2=num%10
    if(n1<n2):
        n1=n2
    num=num//10
print("Largest Number Digit is-",n1)