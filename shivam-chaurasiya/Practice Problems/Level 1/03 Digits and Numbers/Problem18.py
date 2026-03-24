# Check if Digits are in Ascending Order
# Write a program that takes a 3-digit number as input and checks if its digits are in strictly ascending order (e.g., 123 is yes, 132 is no).

num = int(input('Enter a 3-digit number: '))    # 123

last_digit = num % 10
middle_digit = (num // 10) % 10
first_digit = (num // 100) 

if first_digit < middle_digit < last_digit:
    print("Ascending Order")
else:
    print("Not Ascending Order")