# Input and Display Array
# Write a program that takes N numbers as input, stores them in an array, and displays all elements in a single line.


num = int(input('Enter a number: '))

array_list = []

for i in range(num):
    n = int(input())
    array_list.append(n)

print("Array elements in a single line: ")
for i in array_list:
    print(i, end=' ')