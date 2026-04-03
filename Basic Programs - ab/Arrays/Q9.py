#Problem 9: Count Odd Numbers
#Write a program that counts how many odd numbers are in the array
arr=[13,5,7,8,9,6,4,3,2,-1,-67]
odd=0
for i in arr:
    if(i%2!=0):
        odd+=1
print("Odd numbers in array: ",odd)