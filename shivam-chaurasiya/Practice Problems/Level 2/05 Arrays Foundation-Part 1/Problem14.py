# Frequency of Each Element
# Write a program that displays the frequency of each unique element in the array.


arr = [16, 3, 2, 5, 34, 16, 2, 16]
print(f'Array Elements are: {arr}')

my_dict = {}

for num in arr:
    my_dict[num] = my_dict.get(num, 0) + 1
    
for key, value in my_dict.items():
    print(key, ":", value)
