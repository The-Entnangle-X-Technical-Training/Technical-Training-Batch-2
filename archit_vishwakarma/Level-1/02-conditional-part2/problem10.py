year = input("Enter Year : ")

if year.isdigit():
    int_year = int(year) 
    if int_year%4 == 0 and (int_year%100 != 0 or int_year%400 == 0):
        print("Leap year")
    else:
        print("Not Leap Year")
else:
    print("Enter valid year")

