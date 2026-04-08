# Count Positive, Negative, and Zero
# Write a program that counts positive, negative, and zero elements separately in the array

array_list = [-3, 2, -4, 0, 87, -34, 0]

print(f'Array Elements are: ', array_list)

count_positive = 0
count_negative = 0
count_zero = 0

for num in array_list:
    if num > 0:
        count_positive+=1
    elif num < 0:
        count_negative+=1
    else:
        count_zero+=1

print(f'{count_positive} positive numbers are present in the array')
print(f'{count_negative} negative numbers are present in the array')
print(f'{count_zero} zero numbers are present in the array')
    