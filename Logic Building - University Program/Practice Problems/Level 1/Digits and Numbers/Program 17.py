#Program 17: Count Even Digits in a Number

number = int(input("Enter a four digit number: "))

last_digit = number % 10
third_digit = (number // 10) % 10
second_digit = (number // 100) % 10
first_digit = (number // 1000) % 10

even_count = 0

if first_digit % 2 == 0:
    even_count += 1
if second_digit % 2 == 0:
    even_count += 1
if third_digit % 2 == 0:
    even_count += 1
if last_digit % 2 == 0:
    even_count += 1
    
print("Number of even digits: ", even_count)
