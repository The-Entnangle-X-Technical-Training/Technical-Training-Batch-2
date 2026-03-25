num=int(input("Enter number to chek pelindrom:"))
pelin=num
multiple=0
while(num>0):
    nu=num%10
    multiple=(multiple*10)+nu
    num//=10
if(multiple==pelin):
    print("This is pelindrom number")
else:
    print("This is NOT pelindrom number")