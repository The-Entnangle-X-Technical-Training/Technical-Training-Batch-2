#Write a program that takes a single character as input and checks 
#if it is an alphabet (A-Z, a-z), digit (0-9), or special character. Display the result.
char=input("Enter an input: ")
if('a' <= char <='z' or 'A' <= char <= 'Z'):
    print("Character")
elif('0'<=char<='9'):
    print("Digit")
else:
    print("Special Character")