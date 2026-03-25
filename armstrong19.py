num=int(input("Enter number to chek Armstrong number:"))
armstrng=num
multiple=0
while(num>0):
    nu=num%10
    multiple+=nu*nu*nu
    num//=10
if(multiple==armstrng):
    print("This is Armstrong number")
else:
    print("This is NOT Armstrong number")