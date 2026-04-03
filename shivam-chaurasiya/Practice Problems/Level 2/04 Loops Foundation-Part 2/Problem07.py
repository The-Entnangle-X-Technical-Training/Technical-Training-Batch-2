# Nth Fibonacci Number
# Write a program that finds and displays the Nth term of Fibonacci series.
# Example:  1st term: 0, 2nd term: 1, 3rd term: 1, 4th term: 2, 5th term: 3
# Input: N = 5
# Output: 3

n = int(input('Enter a number: '))
a = 0 
b = 1

if n <= 0:
    print('Please enter a positive number.')
elif n == 1:
    print(a)
elif n == 2:
    print(b)
else:
    for _ in range(2, n):
        c = a + b
        a = b
        b = c
    print(b)