input_price=int(input("Enter the Price of the product: "))
quantity=int(input("Enter the quantity of the product: "))
tax_percentage=float(input("Enter the tax percentage: "))
sub_total=input_price*quantity
tax_amount=(sub_total*tax_percentage)/100
total_amount=sub_total+tax_amount
print("Sub total is:",sub_total)
print("Tax amount is: ",tax_amount)
print("Total amount is: ",total_amount)