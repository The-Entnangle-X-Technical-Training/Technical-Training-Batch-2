#Write a program that takes a number and checks 
#if it is divisible by 5. Display "Divisible" or "Not Divisible".
number=int(input("Enter a number: "))
if(number%5==0):
    print(f"{number} is divisible by 5")
else:
    print(f"{number} is not divisible by 5")