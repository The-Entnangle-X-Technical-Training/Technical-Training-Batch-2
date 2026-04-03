#Write a program that counts how many odd numbers exist from 1 to N.
num=int(input("Enter a number: "))
odd=0
for i in range(1,num+1,2):
    if(i%2!=0):
        odd+=1
print(f"First odd numbers from 1 to {num}: ",odd)