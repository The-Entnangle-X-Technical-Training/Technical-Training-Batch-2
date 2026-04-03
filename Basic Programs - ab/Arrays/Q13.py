#Problem 13: Count Positive Numbers 
#Write a program that counts how many positive numbers are in the array.
arr=[13,5,7,8,9,6,4,3,2,-1,-67]
positive=0
for i in arr:
    if(i>0):
        positive += 1
print("Positive numbers in array: ",positive)