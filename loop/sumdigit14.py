num=int(input("Enter number to sum digit:"))
count=0
while(num>0):
    nu=num%10
    count+=nu
    num//=10
print("Total sum of digit is:-",count)