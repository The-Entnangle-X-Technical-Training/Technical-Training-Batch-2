# Prime Number Check
# Write a program that takes a number and checks whether it is prime or not using a loop.
# Hint: Check if the number has any divisor from 2 to N-1

num = int(input('Enter a number: '))    # 11, 4, 9


if num > 1:
    for i in range(2, num): 
        if num % i == 0:
            print(f'{num} is not a prime number')
            break
    else:
        print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')
        
    