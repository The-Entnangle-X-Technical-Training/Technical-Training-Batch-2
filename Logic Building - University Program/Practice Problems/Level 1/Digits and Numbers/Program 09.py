#Program 9: Average of First and Last Digit

number = int(input("Enter a four digit number: "))

last_digit = number % 10
first_digit = number // 1000

average = (first_digit + last_digit) / 2

print("Average of First and Last Digit: ", average)

