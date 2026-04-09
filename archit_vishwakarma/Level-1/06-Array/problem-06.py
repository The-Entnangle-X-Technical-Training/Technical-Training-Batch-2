list = [1,12,3,45,5,66,6,5,0,45,3,2]

smallest = list[0]

for i in range(len(list)):
    if list[i] < smallest:
        smallest = list[i]

print(smallest)
