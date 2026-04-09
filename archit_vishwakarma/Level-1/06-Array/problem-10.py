list = [1,2,3,4,5,6,7,8,9,0]

total = 0
for i in range(len(list)):
    if list[i]%2 == 0:
        total += list[i]

print(total)

