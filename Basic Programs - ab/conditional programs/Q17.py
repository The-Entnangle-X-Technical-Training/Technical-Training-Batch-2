#Write a program that takes a year as input and checks if it is a leap year. A year is leap if divisible by 4.
year=int(input("Enter a year: "))
if(year%4==0):
    print("Leap Year")
else:
    print("Not a Leap year.")