# Display Array in Reverse Order
# Write a program that inputs an array and displays elements in reverse order (without modifying the array).


array_list = [3, 2, 4, 1, 22, 12, 5, 44]
print("Array element withour reverse: ", array_list)
print("Array element in reverse order: ", end='')
for i in array_list[::-1]:
    print(i, end=' ')

