# Profit or Loss Calculator
# Write a program that takes cost price and selling price as input, then determines and displays whether it's profit or loss and calculates the amount.

# Formulas:
# Profit (P) = SP – CP If SP > CP
# Loss (L) = CP – SP If CP > SP
# Profit (P%) = (P/CP) × 100
# Loss (L%) = (L/CP) × 100

cost_price = float(input('Enter the cost price: '))
selling_price = float(input('Enter the selling price: '))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f'Profit: {profit}')
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print(f'Loss: {loss}')
else:
    print('No profit, No loss')