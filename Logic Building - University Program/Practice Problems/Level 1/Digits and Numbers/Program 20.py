#Program 20: Duck Number Checker (4-digit)

number = int(input("Enter a four digit number: "))

last_digit = number % 10
third_digit = (number // 10) % 10
second_digit = (number // 100) % 10
first_digit = (number // 1000) % 10

if first_digit == 0 or second_digit == 0 or third_digit == 0 or last_digit == 0:
    print(number, "is a duck number")
else:
    print(number, "is not a duck number")