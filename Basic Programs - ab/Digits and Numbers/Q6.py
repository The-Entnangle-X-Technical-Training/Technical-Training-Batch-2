#Write a program that takes a 2-digit number as input and displays it in reverse order (e.g., 45 becomes 54).
num=int(input("Enter a 2-digit number: "))
num1=num%10
num2=num//10
print("Reverse order: ",num1*10+num2)