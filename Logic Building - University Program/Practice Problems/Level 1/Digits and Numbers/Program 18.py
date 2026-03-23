#Program 18: Check if Digits are in Ascending Order

number = int(input("Enter a three digit number: "))

last_digit = number % 10
middle_digit = (number // 10) % 10
first_digit = (number // 100) 

if first_digit < middle_digit and first_digit < last_digit and middle_digit < last_digit:
    print("Ascending Order")
else:
    print("Not Ascending Order")
