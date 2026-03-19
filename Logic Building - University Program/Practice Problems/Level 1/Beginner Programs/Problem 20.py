#Problem 20: Profit or Loss Calculator

Cost_price = float(input("Enter the cost price: "))
Selling_Price = float(input("Enter the selling price: "))

calculate = Selling_Price - Cost_price
if calculate > 0:
    print("Profit of", calculate, "rupees")
elif calculate < 0:
    print("Loss of", abs(calculate), "rupees")
else:
    print("There is no profit or loss.")
