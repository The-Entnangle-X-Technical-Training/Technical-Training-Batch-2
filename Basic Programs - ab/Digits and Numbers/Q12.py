#Write a program that takes a 2-digit number as input and checks if it is a palindrome 
#(reads same forwards and backwards). Example: 11 → Yes, 23 → No. Display "Palindrome" or "Not Palindrome".
num=int(input("Enter a 2-digit number: "))
num1=num%10
num2=num//10
if(num1*10+num2==num):
    print("Palindrom")
else:
    print("Not Palindrom")