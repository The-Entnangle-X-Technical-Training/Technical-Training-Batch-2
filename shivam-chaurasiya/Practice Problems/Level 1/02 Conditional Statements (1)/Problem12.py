# Check if Number is Multiple of 3
# Write a program that checks if a number is a multiple of 3. Display "Multiple of 3" or "Not Multiple of 3".

num = int(input('Enter a number: '))

if (num%3==0 and num!=0):
    print('Multiple of 3')
else:
    print('Not Multiple of 3')