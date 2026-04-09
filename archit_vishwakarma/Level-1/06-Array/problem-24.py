list = [1,2,3,4,5,6,7,8,9,10]

print("E : I (ODD)")
for i in range(len(list)):
    if i%2 != 0:
        print(f"{list[i]} : {i}")