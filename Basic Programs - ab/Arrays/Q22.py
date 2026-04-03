#Problem 22: Count Numbers Greater Than 10 
#Write a program that counts how many numbers in the array are greater than 10.
arr=[13,5,7,8,9,6,-2,-80,4,3,2]
count=0
for i in arr:
    if(i>=10):
        count+=1
print("Numbers grater than 10 in array are: ",count)