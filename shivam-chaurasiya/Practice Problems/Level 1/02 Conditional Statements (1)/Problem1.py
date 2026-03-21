# Positive or Negative
# Write a program that takes a number as input and displays whether it is positive or negative.

num = int(input('Enter any number: '))

if (num>0):
    print(f'{num} is a positive number')
elif (num<0):
    print(f'{num} is a negative number')
else:
    print(f'{num} (zero) number')