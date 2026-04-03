#Write a program that takes N as input and prints the first N even numbers.
num=int(input("Enter a number: "))
for num in range(2,num*2+1,2):
    print(f"First {num} even numbers: ",num)