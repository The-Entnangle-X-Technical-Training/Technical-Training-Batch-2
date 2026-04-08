# Find Maximum and Minimum Together
# Write a program that finds both maximum and minimum elements in a single traversal and displays both.

array_list = [-3, 2, -4, 0, 87, -34, 0]
print(f'Array Elements are: ', array_list)

maximum_element = array_list[0]
mininum_element = array_list[0]

for num in array_list:
    if num > maximum_element:
        maximum_element = num
    if num < mininum_element:
        mininum_element = num
    
print(f'Maximum element is: {maximum_element}')
print(f'Minimum element is: {mininum_element}')