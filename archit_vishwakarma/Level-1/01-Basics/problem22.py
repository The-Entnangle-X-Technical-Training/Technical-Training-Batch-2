#Total Cost Calculator

price = float(input("Enter Price : "))
tax_percent = int(input("Enter tax percent : "))
quantity = int(input("Enter Quantity : "))

tax_amt = price*(tax_percent/100)

subtotal = price*quantity

total_amt = (price + tax_amt)*quantity

print(f"Subtotal : {subtotal}")
print(f"Tax amount : {tax_amt}")
print(f"Total amount : {+ total_amt}")