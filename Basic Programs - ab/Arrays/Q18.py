#Problem 18: Count Occurrences of a Number 
#Write a program that counts how many times a specific number X appears in the array.
arr=[12,4,65,87,98,65,4]
print("Array: ",arr)
num=int(input("Enter a number: "))
count=0
for i in arr:
    if(num==i):
        count+=1
print(f"Number appeares in array {count} times.")