#Problem 19: Check if Number is Single Digit

number = int(input("Enter the number: "))

if number >= 0 and number < 10:
    print(number, "is a single digit.")
else:
    print(number, "is not a single digit.")
