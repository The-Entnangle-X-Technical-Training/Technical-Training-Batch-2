#Program 5: Sum of Digits (3-digit number)

number = int(input("Enter a three digit number: "))

last_digit = number % 10 #extract last digit
middle_digit = number // 10 #removes last digit
middle_digit = middle_digit % 10 #extract middle digit
first_digit = number // 100 #extract first digit

sum = first_digit + middle_digit + last_digit
print("first digit:", first_digit, "+ middle digit:", middle_digit, "+ last digit:", last_digit)
print("Sum:", sum)
