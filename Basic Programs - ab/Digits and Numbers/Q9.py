#Write a program that takes a 4-digit number and calculates the average of its first and last digits.
num=int(input("Enter a 4-digit number: "))
num1=num//1000
num2=num%10
avg=(num1+num2)/2
print("Average of first and last digit: ",avg)