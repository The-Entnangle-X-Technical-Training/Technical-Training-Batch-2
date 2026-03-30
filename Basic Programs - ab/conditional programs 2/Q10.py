#Write a program that takes a year as input and checks if it is a leap year.
#A year is leap if divisible by 4 AND (not divisible by 100 OR divisible by 400).
#Display "Leap Year" or "Not Leap Year".
year=int(input("Enter a year: "))
if(year%4==0 and year %100!=0 or year%400==0):
    print("Leap Year")
else:
    print("Not a Leap year.")