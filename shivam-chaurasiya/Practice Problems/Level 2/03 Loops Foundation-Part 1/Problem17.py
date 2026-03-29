# Palindrome Number Check
# Write a program that checks if a number is a palindrome (reads same forwards and backwards). Example: 121, 12321, 1331 are palindromes

num = int(input('Enter a number: '))
palindrom = num
reverse_num = 0

while num > 0:
    r = num % 10
    reverse_num = (reverse_num * 10) + r
    num = num // 10

if palindrom == reverse_num:
    print(f'{palindrom} is a Palindrome.')
else:
    print(f'{palindrom} is not a Palindrome.')