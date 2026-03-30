#Write a program that takes a number as input and displays whether it is positive or negative.
number1=int(input("Enter a number to check if it's Positive or Negative: "))
if(number1>0):
    print("Number is Positive.")
elif(number1==0):
    print("Number is Zero.")
else:
    print("Number is Negative.")