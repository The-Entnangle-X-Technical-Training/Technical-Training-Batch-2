# Product of All Elements
# Write a program that calculates the product of all elements in the array.


array_list = [3, 2, 4, 10]
print(f'Array Elements are: ', array_list)
product = 1

for num in array_list:
    product*=num
    
print(f"The product of all elements is: {product}")