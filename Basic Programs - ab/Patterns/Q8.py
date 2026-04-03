#Inverted Right Triangle - Stars
size=int(input("Enter the size: "))
for i in range(size+1):
    for j in range(i,size):
        print("*",end=' ')
    print()