#  Armstrong Number Check
# Write a program that checks if a number is an Armstrong number (sum of cubes of digits equals the number itself).
# Example: 153, 370, 371, 1634 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153

num_str = input('Enter a number: ')
length = len(num_str)
num = int(num_str)
original_num = num
sum_powers = 0

while num > 0:
    r = num % 10
    sum_powers = (sum_powers + (r**length))
    num = num // 10

if original_num == sum_powers:
    print(f'{original_num} is a Armstrong number')
else:
    print(f'{original_num} is not a Armstrong number')
    

