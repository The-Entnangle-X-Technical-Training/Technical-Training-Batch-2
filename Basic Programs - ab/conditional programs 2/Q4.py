#Write a program that takes two numbers (dividend and divisor) and
#checks if the dividend is divisible by the divisor. Display "Divisible" or "Not Divisible".
num1=int(input("Enter Dividend: "))
num2=int(input("Enter Divisor: "))
if(num1%num2==0):
    print("Divisible")
else:
    print("Not Divisible")