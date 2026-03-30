#Write a program that takes three numbers as input and displays the greatest among them.
number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))
number3=int(input("Enter third number: "))
if(number2<=number1>=number3):
    print(f"{number1} is the greatest among three.")
elif(number1<=number2>=number3):
    print(f"{number2} is the greatest among three.")
else:
    print(f"{number3} is the greatest among three.")