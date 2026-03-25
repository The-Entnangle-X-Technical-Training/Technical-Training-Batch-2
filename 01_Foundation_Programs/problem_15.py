# 33-47 ,58-64, 91-96 special Char
# 48-57 Numbers
# 65-90 UpperCase Alphabets
# 97-122 lowerCase Alphabets

in_char = input("Enter a Character : ")

uni_char = ord(in_char)

if (uni_char >=32 and uni_char <=47) or (uni_char >= 58 and uni_char <=64) or (uni_char >=91 and uni_char <=96):
    print(in_char," is a SPECIAL CHARACTER!")
elif (uni_char >= 48 and uni_char <=57):
    print(in_char," is a NUMBER CHARACTER!")
elif (uni_char >= 65 and uni_char <= 90) or (uni_char >=97 and uni_char <=122):
    print(in_char," is an ALPHABET CHARACTER!")
else:
    print(in_char," is a SPECIAL CHARACTER! or A Character From Different Language")