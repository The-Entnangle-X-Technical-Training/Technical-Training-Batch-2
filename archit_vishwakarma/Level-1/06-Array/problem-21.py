# list = [1,2,3,4,5,6,7,8,9,0]

# list = [9,5,6,4,6,78,3,4,8,6]

list = ['a','b','c','d','e','f','g','h','i','j','k']

a = list[0]
list[0] = list[len(list)-1]
list[len(list)-1] = a

print(list)
print(list[0], list[len(list)-1])