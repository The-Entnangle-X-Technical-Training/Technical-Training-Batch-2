#Write a program that takes a number as input, calculates the sum of its digits, and checks if the number is divisible by 3 using the digit sum rule.
num=int(input("Enter a 3-digit number to check if the sum of digits and number is divisible by 3: "))
num1=num%10
num2=num//10%10
num3=num//100
sum=num1+num2+num3
if(sum%3==0):
    print("sum is divisible by 3 and so the number.")
else:
    print("Sum is not divisible by 3 and so the number.")