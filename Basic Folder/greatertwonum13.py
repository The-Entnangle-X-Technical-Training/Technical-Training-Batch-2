print('Enter 1st Number to chek(greater):',end="")
num1=int(input())
print('Enter 2nd Number to chek(greater):',end="")
num2=int(input())
if (num1==0 and num2==0):
    print("One Number should be Greater Than Zero(0)")
elif num1>num2:
    print(num1,"First Number Is greater than Second Number",num2)
else:
    print(num2,"Second number Is greater than First Number",num1)