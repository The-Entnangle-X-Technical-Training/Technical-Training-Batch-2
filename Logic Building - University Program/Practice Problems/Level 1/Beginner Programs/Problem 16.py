#Problem 16: Days to Years, Weeks, Days Converter

Days = int(input("Enter the total number of days: "))

Years = round(Days/365, 2)
Weeks = round(Days/7, 2)
Remaining_days = Days % 365

print("There are ", Years, "years in ", Days, "days")
print("There are ", Weeks, "weeks in ", Days, "days")
print("There are ", Remaining_days, "remaining days")