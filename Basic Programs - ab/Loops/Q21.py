#Write a program that takes a number and calculates the sum of its digits.
num=int(input("Enter a number: "))
sum=0
if(num==0):
    print("Sum of digits: ",sum)
else:
    while num>0:
        n=num%10
        sum+=n
        num=num//10
print("Sum of all digits: ",sum)