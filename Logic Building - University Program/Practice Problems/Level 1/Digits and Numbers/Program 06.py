#Program 6: Reverse a 2-Digit Number

number = int(input("Enter a two digit number: "))

last_digit = number % 10
first_digit = number // 10

reverse = (last_digit * 10) + first_digit
print("Original number:", number)
print("Reversed number:", reverse)