# Count Distinct Elements
# Write a program that counts how many unique/distinct elements are in the array.

arr = [16, 3, 2, 5, 34, 16, 2, 16]
print(f'Array Elements are: {arr}')

frequency_dict = {}
unique_count = 0


# Method-1
for num in arr:
    frequency_dict[num] = frequency_dict.get(num, 0) + 1
for value in frequency_dict.values():
    if value == 1:
        unique_count+=1
print(f"{unique_count} unique element are in the array")


# Method-2
distinct_count = 0
for num in arr:
    frequency_dict[num] = frequency_dict.get(num, 0) + 1
    
for _ in frequency_dict:
    distinct_count+=1

print(f"{distinct_count} distinct element are in the array")   