#Problem 21: Swap First and Last Element 
#Write a program that swaps the first and last elements of the array.
arr1 = [12, 4, 6, 7, 8,5]
print("Original Array: ",arr1)
n = len(arr1)
for i in range(n // 2):
    arr1[i], arr1[n - i - 1] = arr1[n - i - 1], arr1[i]
    break
print("After swapping first and last element: ",arr1)