#Alphabet Pattern (Single Letter)
#Write a program that prints letter A in triangle pattern for N rows.
size=int(input("Enter the size: "))
for i in range(1,size+1):
    for j in range(i):
        print("A",end=' ')
    print()