# Factorial Calculator
# Write a program that takes a number N and calculates its factorial (N! = 1 × 2 × 3 × ... × N)



def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
num = int(input('Enter a number N: '))   
print(f'The factorial of {num} is: {fact(num)}')