list = [1,2,3,4,5,6,7,7,7,6,9]

p = 0
for i in range(len(list)):
    if p == list[i]:
        print("yes", list[i])
        break
    elif i == (len(list)-1):
        print("No")
    p = list[i]