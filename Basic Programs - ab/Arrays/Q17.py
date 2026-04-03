#Problem 17: Find Position of Minimum
#Write a program that finds at which position (index) the minimum element is located.
arr = [-4,-6,-2,0]

min_val = arr[0]
min_index = 0

for i in range(len(arr)):
    if arr[i] < min_val:
        min_val = arr[i]
        min_index = i

print("Minimum value:", min_val)
print("Position (index):", min_index)