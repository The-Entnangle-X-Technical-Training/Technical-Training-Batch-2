num=int(input("Enter number to count digit:"))
count=0
while(num>0):
    num//=10
    count+=1
print("Total Even Number sum is:-",count)