day = input("Enter a number 1 - 7 : ")

try:
    day = int(day)
    if day >= 1 and day <= 7:
        if day == 1:
            print("Monday")
        elif day == 2:
            print("Tuesday")
        elif day == 3:
            print("Wednesday")
        elif day == 4:
            print("Thursday")
        elif day == 5:
            print("Friday")
        elif day == 6:
            print("Sturday")
        elif day == 7:
            print("Sunday")
    else:
        print("Invalid")
except ValueError:
    print("Enter valid value")
