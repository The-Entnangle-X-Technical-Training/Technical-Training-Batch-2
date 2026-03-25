num=int(input("Enter number sum of ODD:"))
n=0
for i in range(1,num+1):
    if(i%2!=0):
        n+=i
print("Total ODD Number sum is:-",n)