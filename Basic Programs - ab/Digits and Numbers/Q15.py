#Write a program that takes a 4-digit number as input and finds the smallest digit in it, 
#then displays that digit.
num=int(input("Enter a 4-digit number: "))
num1=num%10
num2=num//10%10
num3=num//100%10
num4=num//1000
smallest=num1
if(num2<=smallest):
    smallest=num2
if(num3<=smallest):
    smallest=num3
if(num4<=smallest):
    smallest=num4
print("Smallest digit: ", smallest)