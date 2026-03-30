#Write a program that takes any number as input and checks whether its last digit is even or odd, then displays the result.
num=int(input("Enter a number: "))
last_digit=num%10
if(last_digit%2==0):
    print("Last digit is even.")
else:
    print("Last digit is odd.")