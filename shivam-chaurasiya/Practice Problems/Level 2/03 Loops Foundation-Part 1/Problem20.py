# Strong Number Check
# Write a program that checks if a number is a strong number (sum of factorial of digits equals the number).
# Example: 1, 2, 40585, 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145


num = int(input('Enter a number: '))
original_num = num
fact_sum = 0

# num greater than 0 because 0 is not a Strong number  0!=1
if num > 0:
    while num > 0:
        r = num % 10
        fact = 1
        for i in range(r, 0, -1):
            fact = fact * i  
        fact_sum = fact_sum + fact
        num = num // 10

    if original_num == fact_sum:
        print(f'{original_num} is a Strong Number.')
    else:
        print(f'{original_num} is not a Strong Number.')
else:
    print('Please enter a number greater than 0')



