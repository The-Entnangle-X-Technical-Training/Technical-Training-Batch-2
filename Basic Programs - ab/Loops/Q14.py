#Write a program that counts how many even numbers exist from 1 to N
num=int(input("Enter a number: "))
even=0
for i in range(2,num+1,2):
    if(i%2==0):
        even+=1
print(f"First even numbers from 1 to {num}: ",even)