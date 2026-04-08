# Linear Search
# Write a program that searches for an element X and returns its first position. Display -1 if not found.

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    else:
        return -1
    
arr = [-3, 2, -4, 87, -34, 0]
print(f'Array Elements are: {arr}')
x = int(input('Enter search number: '))

result = linear_search(arr, x)

if result != -1:
    print(f'Element {x} found at index: {result}')
else:
    print("-1") # Not found