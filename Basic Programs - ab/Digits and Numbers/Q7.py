#Write a program that takes a 3-digit number as input and displays it in reverse order (e.g., 456 becomes 654).
num=int(input("Enter a 3-digit number: "))
num1=num%10
num2=num//10%10
num3=num//100
print("Reverse order: ",num1*100+num2*10+num3)