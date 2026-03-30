#Write a program that takes three numbers and checks if they are in strictly ascending order, strictly descending order, or neither.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if(num1==num2==num3):
    print("All numbers are equal.")
elif(num1<num2<num3):
    print("Strictly ascending order.")
elif(num1>num2>num3):
    print("Strictly descending order.")
else:
    print("Neither")