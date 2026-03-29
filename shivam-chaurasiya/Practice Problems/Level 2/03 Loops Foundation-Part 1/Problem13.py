# Count Digits in a Number
# Write a program that takes a number and counts how many digits it has using a loop.
# Hint: Keep dividing by 10 until number becomes 0

num = int(input('Enter a number: '))
n = num 
count = 0

while num > 0:
    r = num % 10 
    count+=1
    num = num // 10
print(f'Number {n} have {count} digits')