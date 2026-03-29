# LCM (Least Common Multiple)
# Write a program that takes two numbers and finds their LCM.
# Hint: LCM × GCD = Product of two numbers

# 4 : 4, 8, 12, 16, 20, 24, 28...
# 6 : 6, 12, 18, 24, 30...
# Common numbers in both: 12, 24, 36 (Least-12)
# LCM of 4 and 6 is = 12
# formula: LCM(a, b) = (a * b) / GCD(a, b)

a = int(input('Enter first number: '))   # 4
b = int(input('Enter second number: '))  # 6

num1, num2 = a, b

while b > 0:
    remainder = a % b
    a = b
    b = remainder

print(f'LCM of {num1} and {num2} is: {(num1 * num2) // a}')



