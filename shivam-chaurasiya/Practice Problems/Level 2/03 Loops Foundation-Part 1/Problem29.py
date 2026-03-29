# GCD (Greatest Common Divisor) / HCF (Highest Common Factor)
# Write a program that takes two numbers and finds their GCD using a loop.
# Hint: Use Euclidean algorithm - keep dividing until remainder becomes 0

"Euclidean algorithm logic: Bade number ko chhote se divide karo, aur jo remainder (shesh) bache, usse purane divisor ko divide karo. Yeh tab tak karo jab tak remainder 0 na aa jaye.                                                            Example: 48 % 18 - Quotient = 2, Remainder = 12, 18 % 12 - Quotient = 1, Remainder = 6, 12 % 6 - Quotient = 2, Remainder = 0"

a = int(input('Enter first number: '))   # 48
b = int(input('Enter second number: '))  # 12

num1, num2 = a, b

while b > 0:
    remainder = a % b
    a = b 
    b = remainder

print(f'The GCD of {num1} and {num2} is: {a}')
    