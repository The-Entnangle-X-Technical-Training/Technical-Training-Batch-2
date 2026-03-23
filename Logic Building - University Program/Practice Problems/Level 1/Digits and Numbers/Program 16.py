#Program 16: Check Divisibility by 3 Using Digit Sum

number = int(input("Enter a four digit number: "))

last_digit = number % 10
third_digit = (number // 10) % 10
second_digit = (number // 100) % 10
first_digit = (number // 1000) % 10

sum = first_digit + second_digit + third_digit + last_digit
print("The sum of digits", number, "is", sum)

if sum % 3 == 0:
    print("The sum of digits", number, "is divisible by 3")
else:
    print("The sum of digits", number, "is not divisible by 3")