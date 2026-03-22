#Program 13: Palindrome Number Checker (3-digit)

number = 565

last = int(number % 10) 
print(last)
mid = int(number / 10)
print(mid)
mid = int(mid % 10)
print(mid)
first = int(number / 100)
print(first)

reverse = last * 100 + mid * 10 + first 
print(reverse)
if number == reverse:
    print("palindrome")
else:
    print("not palindrome")