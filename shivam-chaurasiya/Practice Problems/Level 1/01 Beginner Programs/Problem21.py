# Discount Price Calculator
# Write a program that calculates the final price after applying a discount percentage on the original price(cost price / marked price) ).

# Discount = Marked Price – Selling Price
# Discount (%) = (Discount/MP) × 100


marked_price = float(input('Enter the Marked Price: '))
discount = float(input('Enter the Discount: '))
selling_price = marked_price - (discount/100)*200
print(selling_price)

