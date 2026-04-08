# Average of Array Elements
# Write a program that calculates the average of all array elements and displays it.

array_list = [3, 2, 4, 1]
print(f'Array Elements: ', array_list)
count = 0
total_sum= 0

for num in array_list:
    total_sum+=num
    count+=1

average = total_sum / count
print(f'The average of all elements is: {average}')
    