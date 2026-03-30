#Write a program that takes month number (1-12) and year as input, and displays the number of days in that month (handle leap year for February).
month=int(input("Enter month number: "))
year=int(input("Enter year: "))
if(month==1):
    print("January: 31")
elif(month==2 and ((year%4==0 and year%100!=0) or year%400==0)):
    print("February: 29")
elif(month==2):
    print("February: 28")
elif(month==3):
    print("March: 31")
elif(month==4):
    print("April: 30")
elif(month==5):
    print("May: 31")
elif(month==6):
    print("June: 30")
elif(month==7):
    print("July: 31")
elif(month==8):
    print("August: 31")
elif(month==9):
    print("September: 30")
elif(month==10):
    print("October: 31")
elif(month==11):
    print("November: 30")
elif(month==12):
    print("December: 31")
else:
    print("Invalid Input")