#Program 15: Find Smallest Digit in a Number

number = int(input("Enter a four digit number: "))

last_digit = number % 10
third_digit = (number // 10) % 10
second_digit = (number // 100) % 10
first_digit = (number // 1000) % 10

print(first_digit, second_digit, third_digit, last_digit)

if first_digit < second_digit and first_digit < third_digit and first_digit < last_digit:
    print("first digit is the smallest")
elif second_digit < first_digit and second_digit < third_digit and second_digit < last_digit:
    print("second digit is the smallest")
elif third_digit < first_digit and third_digit < second_digit and third_digit < last_digit:
    print("third digit is the smallest")
else:
    print("fourth digit is the smallest")
    