#Write a program that prints all numbers from 1 to N that are divisible by 3
num=int(input("Enter a number: "))
print(f"Numbers from 1 to {num} that are divisible bye 3 are: ")
for i in range(1,num+1):
    if(i%3==0):
        print(f'{i}')