#Problem 6: Find Minimum Element
#Write a program that finds and displays the smallest element in the array.
arr=[12,5,7,-6,8,-645,999]
smallest=0
for i in arr:
    if(i<smallest):
        smallest=i
print("smallest element: ",smallest)