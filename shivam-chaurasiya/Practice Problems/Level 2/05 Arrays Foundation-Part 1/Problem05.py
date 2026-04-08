# Count Even and Odd Numbers
# Write a program that counts how many even and odd numbers are present in the array separately

array_list = [3, 2, 4, 1, 87, 34, 5]

print(f'Array Elements are: ', array_list)

even_count = 0
odd_count = 0

for num in array_list:
    if num % 2 == 0:
        even_count+=1
    else:
        odd_count+=1

print(f'{even_count} even numbers are present in the array')
print(f'{odd_count} odd numbers are present in the array')
    