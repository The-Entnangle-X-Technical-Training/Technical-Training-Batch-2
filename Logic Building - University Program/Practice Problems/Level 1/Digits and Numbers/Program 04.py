#Program 4: Extract Middle Digit of 3-Digit Number

number = int(input("Enter a three digit number: "))

last_digit = number // 10 #removes last digit.
middle_digit = last_digit % 10 
print("The middle digit is", middle_digit)