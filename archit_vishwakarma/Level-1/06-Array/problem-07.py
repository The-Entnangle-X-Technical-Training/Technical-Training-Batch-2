list = ['a','b','c','d','e',1,2,3,4,5]

reverse = []
for i in range(1, len(list)+1):
    reverse.append(list[-i])

print(reverse)
