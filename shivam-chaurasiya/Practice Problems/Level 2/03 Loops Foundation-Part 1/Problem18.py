# Count Even and Odd Digits
# Write a program that takes a number and counts how many even digits and how many odd digits it contains

num = int(input('Enter a number: '))
number = num
even_digits_count = 0
odd_digits_count = 0

while num > 0:
    r = num % 10
    if r % 2 == 0:
        even_digits_count+=1
    else:
        odd_digits_count+=1
    num = num // 10
    
print(f'Number: {number} has {even_digits_count} even digits and {odd_digits_count} odd digits.')    
