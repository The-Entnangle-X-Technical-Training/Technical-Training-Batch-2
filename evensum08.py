num=int(input("Enter number to sum of even :"))
n=0
for i in range(1,num+1):
    if(i%2==0):
        n+=i
print("Total Even Number sum is:-",n)