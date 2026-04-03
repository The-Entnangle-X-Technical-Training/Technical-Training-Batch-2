#Problem 8: Count Even Numbers 
#Write a program that counts how many even numbers are in the array.
arr=[13,5,7,8,9,6,-2,-80,4,3,2]
even=0
for i in arr:
    if(i%2==0):
        even+=1
print("Even numbers in array: ",even)