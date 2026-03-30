#Write a program that takes day (1-31) and month (1-12) and checks basic validity: day should be 1-31 for most months, 1-30 for Apr/Jun/Sep/Nov, 1-28/29 for Feb. Display "Valid" or "Invalid".
day=int(input("Enter day(1-31): "))
month=int(input("Enter month(1-12): "))
if(1<=day<=31 and month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
    print("Valid")
elif(1<=day<=30 and month==4 or month==6 or month==9 or month==11):
    print("Valid")
elif(1<=day<=28 or 1<=day<=29 and month==2):
    print("Valid")
else:
    print("Invalid")