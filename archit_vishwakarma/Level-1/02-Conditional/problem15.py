char = input("enter a character : ")

check = "vowel" if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' else "consonant"

# better program
#check = "vowel" if char in "aeiou" else "consonant"


print(check)