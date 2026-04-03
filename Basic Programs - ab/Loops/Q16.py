#Write a program that calculates sum of all even numbers from 1 to N.
num=int(input("Enter a number: "))
sum=0
for i in range(1,num+1):
    if(i%2==0):
        sum+=i
print(f'Sum of all even numbers from 1 to {num} is:',sum)