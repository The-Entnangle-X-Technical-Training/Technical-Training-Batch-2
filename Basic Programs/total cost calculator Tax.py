a=int(input("Enter a price of item :"))
b=int(input("Enter a Quantity :"))
c=int(input("Enter a Tax Percentage :"))
subtotal=a*b
tax=(subtotal*c)/100
total=subtotal+tax
print("Subtotal :",subtotal)
print("Tax Amount :",tax)
print("Final Total Amount :",total)