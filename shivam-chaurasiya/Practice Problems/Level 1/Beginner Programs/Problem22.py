# Total Cost Calculator with Tax
# Write a program that calculates total cost of items: input price, quantity, and tax percentage, then calculate and display subtotal, tax amount, and final total amount.

price = float(input('Enter the price: '))
quantity = int(input('Enter the quantity: '))
tax_percentage = int(input('Enter the tax percentage: '))

sub_total = price * quantity
tax_amount = sub_total * (tax_percentage/100)
total_cost = sub_total + tax_amount

print(f'Subtotal: {sub_total}')
print(f'Tax Amount: {tax_amount}')
print(f'Final Total Amount: {total_cost}')