# Reverse a 3-Digit Number
# Write a program that takes a 3-digit number as input and displays it in reverse order (e.g., 456 becomes 654).


num = int(input('Enter a 3-digit number: '))    # 456

r1 = num % 10           # 6
r2 = (num // 10) % 10   # 5
r3 = num // 100         # 4

# :03d ka matlab hai: "3 digits dikhao, agar kam ho toh aage 0 laga do"
print(f'{num:03d} in reverse order is: {r1}{r2}{r3}')