#Write a program that takes a number and checks if it is a single digit (0-9),
#double digit (10-99), or more than double digit. Display the category.
num=int(input("Enter a number: "))
if(0<=num<=9):
    print("Single Digit")
elif(10<=num<=99):
    print("Double Digit")
else:
    print("More than double digit")