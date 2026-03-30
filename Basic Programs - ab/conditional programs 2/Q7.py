#Write a program that takes a single alphabet character 
#and checks if it is uppercase or lowercase. Displaythe result.
char=input("Enter a character: ")
if('a'<=char<='z'):
    print("LowerCase")
elif('A'<=char<='Z'):
    print("Uppercase")
else:
    print("Invalid input")