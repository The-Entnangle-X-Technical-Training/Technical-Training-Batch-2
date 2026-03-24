# Check Leap Year
# Write a program that takes a year as input and checks if it is a leap year. A year is leap if divisible by 4.

year = int(input('Enter a year: '))

if (year%4==0) and (year%100!=0 or year%400==0):
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')