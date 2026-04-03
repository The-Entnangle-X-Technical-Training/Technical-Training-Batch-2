#Write a program that takes a number N as input and prints all numbers from 1 to N.
num=int(input("Enter a value: "))
for num in range(1,num+1):
    print(f'Numbers from 1 to {num}:  ',num)