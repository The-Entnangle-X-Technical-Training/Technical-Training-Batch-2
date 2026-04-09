num=int(input("Enter a 4 digit number :"))
d1=num//1000
d2=(num//100)%10
d3=(num//10)%10
d4=num%10

if(d2==0 or d3==0 or d4==0):
    print("Duck Number")
else:
    print("Not Duck Number")