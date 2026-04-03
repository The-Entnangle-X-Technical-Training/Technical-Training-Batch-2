#Write a program that takes N as input and prints the first N odd numbers.
num=int(input("Enter a number: "))
for num in range(1,num*2,2):
    print(f"First {num} odd numbers: ",num)