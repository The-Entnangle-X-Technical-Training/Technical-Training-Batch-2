# Rotate Array Left by K Positions
# Write a program that rotates the array left by K positions. Example: [1,2,3,4,5], K=2 → [3,4,5,1,2].

nums = [1, 2, 3, 4, 5]
n = len(nums)
k = 2
k = k % n # Agar k, n se bada ho (Safety check)

def reverse(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1 # SUDHAAR: right ko kam karna hai

# Left Rotation Logic:
reverse(nums, 0, k - 1)      # Step 1: Reverse [1, 2] -> [2, 1]
reverse(nums, k, n - 1)      # Step 2: Reverse [3, 4, 5] -> [5, 4, 3]
reverse(nums, 0, n - 1)      # Step 3: Reverse [2, 1, 5, 4, 3] -> [3, 4, 5, 1, 2]

print(f"Array after Left Rotation by {k}:", nums)