#Program 11: Check if Last Digit is Even

number = int(input("Enter a number: "))

last_digit = number % 10

if last_digit % 2 == 0:
    print(last_digit, "is Even")
else:
    print(last_digit, "is odd")