#Problem 7: Display Array in Reverse
#Write a program that displays array elements in reverse order (without modifying the array).
arr1=[12,4,6,7,8]
arr2=[]
for i in arr1:
    arr2.insert(0,i)
print("Array before any change: ",arr1)
print("Reverse Array: ",arr2)