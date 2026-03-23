#Problem 6: Alphabet, Digit, or Special Character

character = input("Enter a single character: ")

# if character >= "A" and character <= "Z":
#     print("alphabet")
# elif character >= "a" and character <= "z":
#     print("alphabet")
# elif character >= "0" and character <= "9":
#     print("digit")
# else:
#     print("special character")

if "A" <= character <= "Z" or "a" <= character <= "z":
    print("Alphabet")
elif "0" <= character <= "9":
    print("Digits")
else:
    print("Special characters")