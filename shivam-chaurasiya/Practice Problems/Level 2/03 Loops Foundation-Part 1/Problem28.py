# Fibonacci Series
# Write a program that takes a number N and prints the first N terms of Fibonacci series (0, 1, 1, 2, 3, 5, 8...).
# Hint: Each term is sum of previous two terms

num = int(input('Enter a number: '))
a = 0
b = 1

if num <= 0:
    print("Please enter a positive number")
elif num == 1:
    print(a)
else:
    print(a, b, end=' ')
    for _ in range(2, num):
        c = a + b
        print(c, end=' ')
        a = b
        b = c     
    