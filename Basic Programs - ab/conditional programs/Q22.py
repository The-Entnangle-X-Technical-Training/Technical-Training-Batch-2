#Write a program that takes cost price and selling price as input and displays whether there is "Profit", "Loss", or "No Profit No Loss".
cost_price=int(input("Enter the cost price: "))
selling_price=int(input("Enter the selling price: "))
if(cost_price>selling_price):
    print("Loss: ",cost_price-selling_price)
elif(cost_price<selling_price):
    print("Profit: ",selling_price-cost_price)
else:
    print("Neither profit nor loss.")