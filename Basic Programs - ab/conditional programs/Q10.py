#Write a program that takes two numbers as input and displays which one is smaller.
number1=float(input("Enter first number: "))
number2=float(input("Enter second number: "))
if(number1==number2):
    print("Numbers are Equal.")
elif(number1<number2):
    print(f"{number1} is smaller then {number2}.")
else:
    print(f"{number2} is smaller then {number1}.")