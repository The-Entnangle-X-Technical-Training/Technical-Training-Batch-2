#Write a program that takes a 3-digit number as input and extracts and displays the first digit.
num=int(input("Enter a 3-digit number: "))
num=num//100
print("First digit: ",num)