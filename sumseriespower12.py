num=int(input("Enter number to sum of series:"))
n=1
c=0
for i in range(2,num+1):
    c=i*2
    n+=c
print("Total Even Number sum is:-",n)