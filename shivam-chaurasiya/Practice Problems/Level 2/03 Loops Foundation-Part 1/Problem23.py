# Print All Prime Numbers from 1 to N
# Write a program that takes a number N and prints all prime numbers from 1 to N.

number = int(input('Enter a number: '))    # 20

if number > 0:
    for num in range(2, number + 1):
        for i in range(2, num):
            if num % i  == 0:
                break
        else:
            print(num, end=' ')
else:
    print(f'{number} is not a prime number')
  
            
