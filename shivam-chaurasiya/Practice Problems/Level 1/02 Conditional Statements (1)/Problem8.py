# Check Divisibility by 5
# Write a program that takes a number and checks if it is divisible by 5. Display "Divisible" or "Not Divisible".

num = int(input('Enter any number: '))

if (num%5)==0:
    print(f'{num} is Divisible by 5')
else:
    print(f'{num} is Not Divisible by 5')