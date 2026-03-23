#Program 14: Find Largest Digit in a Number

number = int(input("Enter a four digit number: "))

last_digit = number % 10
third_digit = (number // 10) % 10
second_digit = (number // 100) % 10
first_digit = (number // 1000) % 10

print(first_digit, second_digit, third_digit, last_digit)

if first_digit > second_digit and first_digit > third_digit and first_digit > last_digit:
    print("first digit is the largest")
elif second_digit > first_digit and second_digit > third_digit and second_digit > last_digit:
    print("second digit is the largest")
elif third_digit > first_digit and third_digit > second_digit and third_digit > last_digit:
    print("third digit is the largest")
else:
    print("fourth digit is the largest")
    