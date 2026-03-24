# Simple Discount Calculator
# Write a program that gives discount based on purchase amount:
# If amount >= 1000: 10% discount
# Otherwise: No discount Display final amount after discount.

purchase_amount = float(input('Enter the purchase amount: '))

if purchase_amount >= 1000:
    discount = purchase_amount*10/100
    final_amount = purchase_amount - discount
else:
    final_amount = purchase_amount
print('Final Amount:', final_amount) 