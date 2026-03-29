#  Product of Digits
# Write a program that takes a number and calculates the product of all its digits using a loop. (Example: enter a number: 123, product its digits: 1 * 2 * 3 = 6)

num = int(input('Enter a number: '))    # 123
n = num
product_digit = 1

while num > 0:
    r = num % 10
    product_digit = product_digit * r
    num = num // 10
print(f'The product of digits of {n} is: {product_digit}')


# *************************************************************************
num_str = input('Enter a number: ') 
product_digit = 1

for char in num_str:
    digit = int(char)    
    product_digit = product_digit * digit

print(f'The product of digits of {num_str} is: {product_digit}')
    