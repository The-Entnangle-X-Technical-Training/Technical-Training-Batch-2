# Print 1 to N
# Write a program that takes a number N as input and prints all numbers from 1 to N.


num = int(input('Enter a number N: '))

for i in range(1, num+1):
    print(i, end=' ')