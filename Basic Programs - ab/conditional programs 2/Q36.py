#Write a program that takes password length, count of uppercase letters, lowercase letters, 
#and digits as separate inputs. Check if password is Strong (length≥8, has uppercase, lowercase,
#digits), Medium (length≥6, any 2 types), or Weak.
length=int(input("Enter the length of password: "))
uppercase=int(input("Enter the number of uppercase in the password: "))
lowercase=int(input("Enter the number of lowercase in the password: "))
digit=int(input("Enter how many digits are in the password: "))
if(uppercase+lowercase+digit)>length:
    print("Invalid input: The sum of character types cannot be greater than the total length.")
else:
    if(length>=8 and uppercase>0 and lowercase>0 and digit>0):
        print("Strong Password")
    elif(length>=6 and ((uppercase > 0 and lowercase > 0) or  (uppercase > 0 and digit > 0) or (lowercase > 0 and digit > 0))):
        print("Medium Password")
    else:
        print("Weak Password")