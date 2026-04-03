#Problem 25: Check if Array has Duplicates 
#Write a program that checks if any number appears more than once in the array. Display "Yes" or "No".
arr = [12, 4, 6, 7, 8, 4]
print("Array:",arr)
duplicate = False
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            duplicate = True
            break
    if duplicate:
        break
if duplicate:
    print("Yes")
else:
    print("No")