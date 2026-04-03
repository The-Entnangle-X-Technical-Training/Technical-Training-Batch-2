# Check if Two Numbers are Co-Prime
# Write a program that takes two numbers and checks if they are co-prime (GCD = 1)

# 1. Co-Prime Numbers Kya Hain?
# Do numbers tab Co-Prime hote hain jab unke beech '1' ke alawa aur koi bhi Common Factor na ho. Matlab, unka GCD (Greatest Common Divisor) hamesha 1 hona chahiye.

# Example: 8 aur 15
# 8 ke factors: 1, 2, 4, 8
# 15 ke factors: 1, 3, 5, 15
# Common Factor: only 1.
# GCD: 1
# Result: 8 and 15 is Co-Prime.


a = int(input('Enter first number: '))   # 8
b = int(input('Enter second number: '))  # 15

num1, num2 = a, b

while b > 0:
    remainder = a % b
    a = b
    b = remainder

if a == 1:
    print(f'{num1} and {num2} are Co-Prime')
else:
    print(f'{num1} and {num2} are not Co-Prime')