# Table Generator
# Write a program that takes a number N and prints its multiplication table from 1 to 10

num = int(input('Enter a number N: '))

for i in range(1, num):
    print(f'{num}*{i} = {num*i}')
    if i==10:
        break