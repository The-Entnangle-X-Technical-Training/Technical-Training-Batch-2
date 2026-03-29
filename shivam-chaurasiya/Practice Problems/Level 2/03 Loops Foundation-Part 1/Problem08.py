# Sum of First N Even Numbers
# Write a program that takes a number N and calculates the sum of first N even numbers.

num = int(input('Enter a number N: '))
even_sum = 0

for i in range(0, num * 2, 2):
    even_sum+=i 
    
print(f'The sum of first {num} even numbers is {even_sum}.')