print('Enter 1st Number:',end="")
num1=int(input())
print('Enter 2nd Number:',end="")
num2=int(input())
print('Enter 3rd Number:',end="")
num3=int(input())
if(num1<num2):
    if(num2<num3):
        print("The Greatest Number is Num3",num3)
    else:
        print("The Greatest Number is Num2",num2)
elif(num1<num3):
     print("The Greatest Number is Num1",num3)
else:
    print("The Greatest Number is Num1",num1)