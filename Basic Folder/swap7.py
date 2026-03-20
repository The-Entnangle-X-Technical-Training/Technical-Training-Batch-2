print('Enter 1st Number:',end="")
a=int(input())
print('Enter 2nd Number:',end="")
b=int(input())
print("Before Swap:")
print("1st Number=",a)
print("2nd Number=",b)
a=a+b
b=a-b
a=a-b
print("After Swap:")
print("1st Number=",a)
print("2nd Number=",b)