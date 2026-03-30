#Write a program that takes a 3-digit number, calculates the sum of its digits, and checks 
#if the number is divisible by this sum. Example: 153 → 1+5+3=9, 153÷9=17 → Harshad Number. 
#Display "Harshad Number" or "Not Harshad Number".
num=int(input("Enter a 3-digit number: "))
num1=num%10
num2=num//10%10
num3=num//100
sum=num1+num2+num3
if(num%sum==0):
    print("Harshad Number")
else:
    print("Not Harshad Number")