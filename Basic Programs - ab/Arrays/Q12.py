#Problem 12: Search for a Number 
#Write a program that takes a number X and checks if it exists in the array. Display "Found" or "Not Found".
arr=[12,3,456,768,9]
print(arr)
num=int(input("Enter a number: "))
for i in arr:
    if(num==i):
        print("Found")
        break
    else:
        print("Not Found")
        break