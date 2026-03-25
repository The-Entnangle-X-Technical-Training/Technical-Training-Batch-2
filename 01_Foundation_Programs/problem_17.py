year = int(input("Enter an Year : "))

if(year % 4 == 0 or year % 400 ==0) and year % 100 != 0:
    print(year,"is a LEAP-YEAR!")
else:
    print(year,"is NOT a LEAP-YEAR!")