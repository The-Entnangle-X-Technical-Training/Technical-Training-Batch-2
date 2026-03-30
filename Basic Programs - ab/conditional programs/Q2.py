#Write a program that takes a number as input and displays whether it is even or odd.
number=int(input("Enter a number: "))
if(number==0):
    print("Number is Zero.")
elif(number%2==0):
    print("Number is Even.")
else:
    print("Number is Odd.")