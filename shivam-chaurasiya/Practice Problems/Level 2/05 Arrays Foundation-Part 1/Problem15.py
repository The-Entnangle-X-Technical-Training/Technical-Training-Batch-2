# Reverse Array (In-Place)
# Write a program that reverses the array by modifying it. Example: [1,2,3,4,5] becomes [5,4,3,2,1]


arr = [1, 2, 3, 4, 5]
n = len(arr)    # 5

for i in range(n//2):
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    
print(arr)