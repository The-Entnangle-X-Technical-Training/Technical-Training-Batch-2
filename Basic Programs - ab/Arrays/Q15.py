#Problem 15: Average of Array Elements 
#Write a program that calculates the average of all array elements.
arr=[13,5,7,8,9,6,-2,-80,4,3,2]
sum=0
for i in arr:
        sum+=i
print("Average of all array elements: ",sum/len(arr))