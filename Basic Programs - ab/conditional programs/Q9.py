#Write a program that takes a number and checks
#if it is divisible by 10. Display "Divisible" or "Not Divisible".
number=int(input("Enter a number: "))
if(number%10==0):
    print(f"{number} is divisible by 10")
else:
    print(f"{number} is not divisible by 10")