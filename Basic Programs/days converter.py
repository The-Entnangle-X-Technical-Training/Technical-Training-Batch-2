a=int(input("Enter a total number of Days :"))
years=a//365
days=a%365
weeks=days//7
days_left=days%7
print("Years :",years)
print("Weeks :",weeks)
print("Days :",days_left)