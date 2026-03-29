# Print All Factors of a Number
# Write a program that takes a number as input and prints all its factors using a loop.

number = int(input('Enter a number: ')) 

for i in range(1, number+1):
    if number % i == 0:
        print(i, end=' ')