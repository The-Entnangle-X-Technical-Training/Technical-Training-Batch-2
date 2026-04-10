# Swap First and Last Element
# Write a program that swaps the first and last elements of the array.



print("Before swaps the first and last element of the array")
arr = [1, 2, 3, 4, 5]
print(arr)

print("After swaps the first and last element of the array")
arr[0], arr[-1] = arr[-1], arr[0]
print(arr)

