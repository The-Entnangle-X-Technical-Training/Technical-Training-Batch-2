# Check if Number is Single Digit
# Write a program that checks if a number is a single digit (0-9). Display "Single Digit" or "Not Single Digit".
    
num = int(input('Enter a number: '))
    
if 0 <= num <= 9 or -9 <= num <= 0:
    print(f'Single Digit')
else:
    print(f'Not Single Digit')