#Program 19: Harshad/Niven Number Checker (3-digit)

number = int(input("Enter a three digit number: "))

last_digit = number % 10
middle_digit = (number // 10) % 10
first_digit = (number // 100)

sum = first_digit + middle_digit + last_digit

if number % sum == 0:
    print(number, "is a harshad number")
else:
    print(number, "is not a harshad number")
    