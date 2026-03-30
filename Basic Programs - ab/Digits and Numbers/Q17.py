#Write a program that takes a 4-digit number as input and counts how many of its digits are even, then displays the count.
num=int(input("Enter a 4-digit number: "))
num1=num%10
num2=num//10%10
num3=num//100%10
num4=num//1000
even=0
if(num1%2==0):
    even+=1
if(num2%2==0):
    even+=1
if(num3%2==0):
    even+=1
if(num4%2==0):
    even+=1
print("Number of even digits in number: ",even)