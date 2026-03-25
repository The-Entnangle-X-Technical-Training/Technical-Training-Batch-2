num=int(input("Enter base number  :"))
num1=int(input("Enter exponent number  :"))
multiple=1
for i in range(1,num1+1):
    multiple*=num
print("The calculate of exponent:-",multiple)