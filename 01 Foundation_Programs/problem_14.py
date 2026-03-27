char = input("Enter an Alphabet : ")

vowels = ['a','e','i','o','u']

in_char = char.lower()
is_vowel = False
for ch in vowels :
    if ch == in_char :
        is_vowel = True

if is_vowel == True :
    print("Given Alphabet ",char,"is a VOWEL!")
else :
    print("Given Alphabet ",char,"is a CONSONENT!")