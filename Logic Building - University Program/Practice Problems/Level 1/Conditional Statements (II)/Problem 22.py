#Problem 22: Month Days Calculator

Month_Number = int(input("Enter the month number: "))
year = int(input("Enter the year: "))

if Month_Number == 1:
    print("Month 1 is january and it has 31 days")
elif Month_Number == 2:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year, "is a leap year and it has 29 days.")
    else:
        print(year, "is not a leap year and has 28 days.")
elif Month_Number == 3:
    print("Month 3 is march and it has 31 days.")
elif Month_Number == 4:
    print("Month 4 is april and it has 30 days.")
elif Month_Number == 5:
    print("Month 5 is may and it has 31 days.")
elif Month_Number == 6:
    print("Month 6 is june and it has 30 days.")
elif Month_Number == 7:
    print("Month 7 is july and it has 31 days.")
elif Month_Number == 8:
    print("Month 8 is august and it has 31 days.")
elif Month_Number == 9:
    print("Month 9 is september and it has 30 days.")
elif Month_Number == 10:
    print("Month 10 is october and it has 31 days.")
elif Month_Number == 11:
    print("Month 11 is november and it has 30 days.")
elif Month_Number == 12:
    print("Month 12 is december and it has 31 days.")
else:
    ("invalid")