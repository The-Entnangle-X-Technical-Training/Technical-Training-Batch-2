#Write a program that checks if a number is divisible by both 2 and 3. Display "Yes" or "No".
num=int(input("Enter a number: "))
if(num%2==0 and num%3==0):
    print("Yes")
else:
    print("No")