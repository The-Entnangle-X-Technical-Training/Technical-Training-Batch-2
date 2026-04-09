list = [1,12,3,45,5,66,6,5,45,3,2]

greater = list[0]

for i in range(len(list)):
    if list[i] > greater:
        greater = list[i]

print(greater)
