# Count Occurrences of Element
# Write a program that counts how many times a specific element X appears in the array.

def count_occurrences(arr, target):
    count = 0
    for i in range(len(arr)):
        if arr[i] == target:
            count+=1
    print(f'Element {target} appears {count} times in the array')

arr = [16, 3, 2, 5, 34, 16, 2, 16]
print(f'Array Elements are: {arr}')
target = int(input('Enter a number: '))
count_occurrences(arr, target)