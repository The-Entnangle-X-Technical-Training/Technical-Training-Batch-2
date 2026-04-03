# #Problem 20: Reverse Array (In-Place) 
# #Write a program that reverses the array by modifying it. Example: [1,2,3,4,5] becomes [5,4,3,2,1].
arr1 = [12, 4, 6, 7, 8,5]
print("Original Array: ",arr1)
n = len(arr1)
for i in range(n // 2):
    arr1[i], arr1[n - i - 1] = arr1[n - i - 1], arr1[i]
print("Array after modification: ",arr1)