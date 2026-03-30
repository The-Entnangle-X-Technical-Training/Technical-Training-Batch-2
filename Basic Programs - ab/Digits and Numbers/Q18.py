#Write a program that takes a 3-digit number as input and checks if its digits are in strictly ascending order (e.g., 123 is yes, 132 is no).
num=int(input("Enter a 3-digit number: "))
num1=num//100
num2=num//10%10
num3=num%10
if(num1<num2<num3):
    print("Ascending order")
else:
    print("Not")