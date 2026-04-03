#Problem 11: Continuous Number Pattern
#Write a program that prints continuous numbers in triangle pattern for N rows.
size=int(input("Enter the size: "))
num=1
for i in range(1,size+1):
    for j in range(i):
        print(num,end=' ')
        num+=1
    print()