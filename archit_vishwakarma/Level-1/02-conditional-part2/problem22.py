month = input("Enter a month in number : ")
year = input("Enter year : ")

if month.isdigit() and year.isdigit():
    month = int(month)
    year = int(year)

    if month >= 1 and month <= 12:
        if month == 1:
            result = 31
        elif month == 2:
            if year%4 == 0 and year%100 != 0 or year%400 == 0:
                result = 29
            else:
                result = 28
        elif month == 3:
            result = 31
        elif month == 4:
            result = 30
        elif month == 5:
            result = 31
        elif month == 6:
            result = 30
        elif month == 7:
            result = 31
        elif month == 8:
            result = 31
        elif month == 9:
            result = 30
        elif month == 10:
            result = 31
        elif month == 11:
            result = 30
        elif month == 12:
            result = 31

        if result == 29:
            x = "Because of Leap Year."
        else:
            x = ""
        print(f"for month {month} in year {year} there are {result} days. {x}")
    else:
        print("Invalid")
else:
    print("Enter valid value")
