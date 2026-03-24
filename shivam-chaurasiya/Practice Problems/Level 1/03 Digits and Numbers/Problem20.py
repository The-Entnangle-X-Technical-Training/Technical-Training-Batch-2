# Duck Number Checker (4-digit)
# Write a program that takes a 4-digit number ABCD and checks if it contains the digit 0 anywhere except the first position. Example: 4012 → Duck Number, 0123 → Not Duck, 1234 → Not Duck. Display "Duck Number" or "Not Duck Number".

num = int(input('Enter a 4-digit number: '))    # 4012


last_digit = num % 10 
third_digit = (num // 10) % 10
second_digit = (num // 100) % 10

if second_digit == 0 or third_digit == 0 or last_digit == 0:
    print("Duck Number")
else:
    print("Not Duck Number")