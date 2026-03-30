#Write a program that takes a 4-digit number as input and finds the largest digit in it, then displays that digit.
num=int(input("Enter a 4-digit number: "))
num1=num%10
num2=num//10%10
num3=num//100%10
num4=num//1000
largest=num1
if(num2>=largest):
    largest=num2
if(num3>=largest):
    largest=num3
if(num4>=largest):
    largest=num4
print("Largest digit: ", largest)