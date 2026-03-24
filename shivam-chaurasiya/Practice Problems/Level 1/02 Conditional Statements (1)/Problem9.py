# Check Divisibility by 10
# Write a program that takes a number and checks if it is divisible by 10. Display "Divisible" or "Not Divisible".


num = int(input('Enter any number: '))

if (num%10)==0:
    print(f'{num} is Divisible by 10')
else:
    print(f'{num} is Not Divisible by 10')