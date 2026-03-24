# Positive, Negative, or Zero
# Write a program that takes a number as input and displays whether it is positive, negative, or zero.


num = int(input('Enter a number: '))

if num>0:
    print(f'{num} is a positive number')
elif num<0:
    print(f'{num} is a negative number')
else:
    print(f'{num} is a zero number')