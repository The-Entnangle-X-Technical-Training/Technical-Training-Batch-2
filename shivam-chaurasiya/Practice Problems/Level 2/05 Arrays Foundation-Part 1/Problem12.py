# Check for Duplicates
# Write a program that checks if any element appears more than once in the array. Display "Yes" or "No".

arr = [16, 3, 2, 5, 34, 16, 2, 16]
# arr = [16, 3, 2, 5]
print(f'Array Elements are: {arr}')

frequency_dict = {}

for num in arr:
    # frequency_dict.get(num, 0) ka matlab: num dhoondo, nahi mila toh 0 maan lo
    frequency_dict[num] = frequency_dict.get(num, 0) + 1
    if frequency_dict[num] > 1:
        print(f"Yes")  
        break
else:
    print('No')

