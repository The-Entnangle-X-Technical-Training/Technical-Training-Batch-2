#Program 3: Extract First Digit of 3-Digit Number

number = int(input("Enter a three digit number: "))

extract = number // 100 ##division int doesn't show the digits after decimal

print("The first digit is ", extract)
