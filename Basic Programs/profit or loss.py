a=int(input("Enter a Cost Price :"))
b=int(input("Selling Price :"))
if(b>a):
    profit=b-a
    print("Profit")
    print("Amount :",profit)
elif(b<a):
    loss=a-b
    print("Loss")
    print("Amount :",loss)
else:
    print("No profit No loss")