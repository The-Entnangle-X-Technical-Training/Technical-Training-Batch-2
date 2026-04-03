# Right Triangle - Stars (Increasing)
size=int(input("Enter the size of Right Triangle: "))
for i in range(1,size+1):
    for j in range(i):
        print("*",end=" ")
    print()