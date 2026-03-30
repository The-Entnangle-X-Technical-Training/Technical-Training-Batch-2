#Write a program that takes a 3-digit number as input and checks if it is a palindrome. 
#Example: 121 → Yes, 123 → No. Display "Palindrome" or "Not Palindrome".
num=int(input("Enter a 3-digit number: "))
num1=num%10
num2=num//10%10
num3=num//100
if(num1*100+num2*10+num3==num):
    print("Palindrom")
else:
    print("Not Palindrom")