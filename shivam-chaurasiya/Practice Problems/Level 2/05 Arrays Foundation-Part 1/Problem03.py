# Sum of Array Elements
# Write a program that calculates and displays the sum of all elements in an array.

array_list = [3, 2, 4, 1]
print(f'Array Elements: ', array_list)

total_sum= 0

for num in array_list:
    total_sum+=num
    
print(f'The sum of all elements is: {total_sum}')
    