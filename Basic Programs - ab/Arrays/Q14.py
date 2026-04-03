#Problem 14: Count Negative Numbers
#Write a program that counts how many negative numbers are in the array.
arr=[13,5,7,8,9,6,4,3,2,-1,-67]
negative=0
for i in arr:
    if(i<0):
        negative += 1
print("Negative numbers in array: ",negative)