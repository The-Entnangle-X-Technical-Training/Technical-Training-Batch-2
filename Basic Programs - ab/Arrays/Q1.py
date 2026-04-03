#Problem 1: Input and Display Array
#Write a program that takes 5 numbers as input, stores them in an array, and displays all elements.
arr=[]
for i in range(5):
    val=int(input(f"Enter {i+1} number: "))
    arr.append(val)
print(arr)
