#Problem 22: Total Cost Calculator with Tax

Price = float(input("Enter the original price of the item: "))
Quantity = float(input("Enter the quantity of the item: "))
Tax = float(input("Enter the tax percentage: "))

Subtotal = Price * Quantity
Tax_Amount = (Subtotal * Tax)/100
Total_Amount = Subtotal + Tax_Amount

print("Subtotal amount of the item/items: ", Subtotal)
print("Total tax amount: ", Tax_Amount)
print("final amount: ", Total_Amount)
