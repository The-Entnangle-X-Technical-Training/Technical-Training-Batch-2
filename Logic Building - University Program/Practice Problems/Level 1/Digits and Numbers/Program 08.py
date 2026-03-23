#Program 8: Swap First and Last Digit of 3-Digit Number

number = int(input("Enter a three digit number: "))

last_digit = number % 10 #extract last digit
middle_digit = number // 10 #removes last digit
middle_digit = middle_digit % 10 #extract middle digit
first_digit = number // 100 #extract first digit

swap = last_digit * 100 + middle_digit * 10 + first_digit
print("After swap:", swap)

