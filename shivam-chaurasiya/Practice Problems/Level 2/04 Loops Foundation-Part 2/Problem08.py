# Check if Number is Fibonacci Number
# Write a program that checks if a given number exists in the Fibonacci series by generating terms until reaching or exceeding the number.

n = int(input('Enter a number: '))
a = 0 
b = 1

if n in {0, 1}:
    print(f'{n} exists in the fibonacci series.')
else:
    while b < n:
        c = a + b
        a = b
        b = c
    if b == n:
        print(f'{n} exists in the Fibonacci series.')
    else:
        print(f'{n} does NOT exist in the Fibonacci series.')
