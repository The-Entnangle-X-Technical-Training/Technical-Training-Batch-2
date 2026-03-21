# Check Vowel or Consonant
# Write a program that takes a single character as input and checks if it is a vowel (a, e, i, o, u) or consonant.

char = input('Enter a character: ')

vow = 'aeiouAEIOU'
conso = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

if char in vow:
    print(f'{char} is a vowel.')
elif char in conso:
    print(f'{char} is a consonant.')
else:
    print(f'{char} is neither a vowel nor a consonant.')
    