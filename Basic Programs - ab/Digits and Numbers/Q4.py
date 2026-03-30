#Write a program that takes a 3-digit number as input and extracts and displays the middle digit.
num=int(input("Enter a 3-digit number: "))
digit=num//10
digit=digit%10
print("Middle digit: ",digit)