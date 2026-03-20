print('Enter 1st Number:',end="")
num1=int(input())
print('Enter 2nd Number:',end="")
num2=int(input())
print('Enter 3rd Number:',end="")
num3=int(input())
if(num1<num2):
    if(num2<num3):
        print("The Smallest Number is Num1",num1)
    else:
        print("The Smallest Number is Num3",num3)
elif(num2<num3):
     print("The Smallest Number is Num2",num2)
else:
    print("The Smallest Number is Num3",num3)