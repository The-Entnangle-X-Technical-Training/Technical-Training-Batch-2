# Perfect Number Check
# Write a program that checks if a number is a perfect number (sum of its divisors excluding itself equals the number).
# Example: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14

num = int(input('Enter a number: '))    # 6
divisors_sum = 0

for i in range(1, num):
    if num % i == 0:
        divisors_sum+=i
        
if divisors_sum == num:
    print(f'{num} is a perfect number.')
else:
    print(f'{num} is not a perfect number.')
        
    