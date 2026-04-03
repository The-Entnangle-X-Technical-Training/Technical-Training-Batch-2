#Problem 11: Sum of Odd Numbers 
#Write a program that calculates the sum of only odd numbers in the array.
arr=[12,4,65,87,98,65,4]
sum=0
for i in arr:
    if(i%2!=0):
        sum+=i
print("Sum of all odd numbers in the array is: ",sum)