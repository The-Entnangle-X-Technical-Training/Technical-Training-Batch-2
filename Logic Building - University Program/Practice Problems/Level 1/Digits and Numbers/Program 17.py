#Program 17: Count Even Digits in a Number

number = int(input("Enter a four digit number: "))

last_digit = number % 10
third_digit = (number // 10) % 10
second_digit = (number // 100) % 10
first_digit = (number // 1000) % 10

