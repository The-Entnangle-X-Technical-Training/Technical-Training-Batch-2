# Count Prime Numbers (1 to N)
# Write a program that takes a number N and counts how many prime numbers exist from 1 to N.


number = int(input('Enter a number: '))    # 20
count = 0

if number > 0:
    for num in range(2, number + 1):
        for i in range(2, num):
            if num % i  == 0:
                break
        else:
            count+=1

print(f'{count} prime numbers exist between 1 and {number}')