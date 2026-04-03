#Write a program that takes a number N and prints its multiplication table from N×1 to N×10.
num=int(input("Enter a number: "))
for i in range(1,11):
    print(f'{num}*{i}={num*i}')