# Find All Positions of Element
# Write a program that displays all positions where element X appears in the array.


arr = [16, 3, 2, 5, 34, 16, 2, 16]
print(f'Array Elements are: {arr}')
target = int(input('Enter a number: '))
position = []

for i in range(len(arr)):
    if arr[i] == target:
        position.append(i)

if len(position) == 0:
    print(f'Element {target} is not present any position in the array')
else:
    print(f'Element {target} found at position: {position}')
    # print(f"Element {target} found at position: ", *position)