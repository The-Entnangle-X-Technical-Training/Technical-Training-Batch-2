# Print N to 1
# Write a program that takes a number N as input and prints all numbers from N to 1 in reverse order.

num = int(input('Enter a number N: '))

for i in range(num, 0, -1):
    print(i, end=' ')