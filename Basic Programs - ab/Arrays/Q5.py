#Problem 5: Find Maximum Element
#Write a program that finds and displays the largest element in the array.
arr=[12,5,7,-6,8,-645,999]
largest=0
for i in arr:
    if(i>largest):
        largest=i
print("Largest element: ",largest)