days=int(input("Enter the number of days you want to calculate: "))
years=days//365
weeks=int((days%365)/7)
rem_days=int(days-(years*365))%7
print("Years: ",years)
print("Weeks: ",weeks)
print("Days: ",rem_days)