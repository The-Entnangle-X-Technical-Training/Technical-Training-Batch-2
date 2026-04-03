# Sum of Fibonacci Series
# Write a program that calculates the sum of first N Fibonacci numbers.

num = int(input('Enter a number: '))

a = 0
b = 1
fibonacci_sum = 0

if num <= 0:
    print('Please enter a positive number')
else:
    for _ in range(num):
        fibonacci_sum+=a
        c = a + b
        a = b
        b = c
        
    print(f'The sum of first {num} Fibonacci numbers is: {fibonacci_sum}')
