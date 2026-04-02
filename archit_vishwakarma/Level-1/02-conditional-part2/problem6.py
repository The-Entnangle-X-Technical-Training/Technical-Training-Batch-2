char = input("Enter a single char : ")
char_ascii = ord(char)
if char_ascii>= 65 and char_ascii <= 90 or char_ascii>= 97 and char_ascii<=122:
    print("Alphabet")
elif char_ascii>= 48 and char_ascii<=57:
    print("number")
else:
    print("Special chracter")