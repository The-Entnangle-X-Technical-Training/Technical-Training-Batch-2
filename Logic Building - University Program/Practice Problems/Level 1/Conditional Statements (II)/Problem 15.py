number = int(input("Enter a number: "))

if 0 <= number <= 9:
    print("single digit")
elif 10 <= number <= 99:
    print("double digit")
else:
    print("more than two digits")