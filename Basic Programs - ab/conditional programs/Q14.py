#Write a program that takes three numbers as input and displays the smallest among them.
number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))
number3=int(input("Enter third number: "))
if(number1<=number2<=number3):
    print(f"{number1} is the smallest among three.")
elif(number2<=number1<=number3):
    print(f"{number2} is the smallest among three.")
else:
    print(f"{number3} is the smallest among three.")