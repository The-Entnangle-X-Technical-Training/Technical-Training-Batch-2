num=int(input("Enter number to product of digit:"))
multiple=1
while(num>0):
    nu=num%10
    multiple=multiple*nu
    num//=10
print("The product of digit is:-",multiple)