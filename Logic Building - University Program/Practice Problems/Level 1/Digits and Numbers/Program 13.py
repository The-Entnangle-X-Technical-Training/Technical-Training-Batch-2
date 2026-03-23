#Program 13: Palindrome Number Checker (3-digit)

number = int(input("Enter a number: "))

last = number % 10 
mid = number // 10
mid = mid % 10
first = number // 100

reverse = last * 100 + mid * 10 + first 
print(reverse)
if number == reverse:
    print("palindrome")
else:
    print("not palindrome")
    