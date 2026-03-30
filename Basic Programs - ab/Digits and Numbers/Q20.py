#Write a program that takes a 4-digit number ABCD and checks if it contains the digit 0 anywhere
#except the first position. Example: 4012 → Duck Number, 0123 → Not Duck, 1234 → Not Duck.
#Display "Duck Number" or "Not Duck Number".
num=int(input("Enter a 4-digit number: "))
num1=num%10
num2=num//10%10
num3=num//100%10
num4=num//1000
if(num4==0):
    print("Not Duck Number")
elif(num1==0 or num2==0 or num3==0):
    print("Duck Number")
else:
    print("Not Duck Number")