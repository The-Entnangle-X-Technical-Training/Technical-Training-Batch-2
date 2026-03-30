#Write a program that takes a 3-digit number as input and calculates the sum of all its digits, then displays the result.
num=int(input("Enter a 3-digit number: "))
num1=num//100
num2=num//10%10
num3=num%10
print("Sum of all digits: ",num1+num2+num3)