#Write a program that takes a number and counts how many digits it has.
num=int(input("Enter a number: "))
digit=0
if(num==0):
    digit = 1
else:
    while num>0:
        num=num//10
        digit += 1
print(f'Digits in number {num}: ',digit)