#Program 12: Palindrome Number Checker (2-digit)

number = int(input("enter a two digit number: "))

last_digit = number % 10
first_digit = number // 10

reverse = last_digit * 10 + first_digit

if number == reverse:
    print("Palindrome")
else:
    print("Not palindrome")
    