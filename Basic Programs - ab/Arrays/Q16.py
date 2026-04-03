#Problem 16: Find Position of Maximum 
#Write a program that finds at which position (index) the maximum element is located.
arr = [-4,-6,-2,0]

max_val = arr[0]
max_index = 0

for i in range(len(arr)):
    if arr[i] > max_val:
        max_val = arr[i]
        max_index = i

print("Maximum value:", max_val)
print("Position (index):", max_index)