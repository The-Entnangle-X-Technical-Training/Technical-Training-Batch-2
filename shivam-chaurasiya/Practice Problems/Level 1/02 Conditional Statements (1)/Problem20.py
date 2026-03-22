# Electricity Bill (Simple)
# Write a program that calculates electricity bill:
# If units <= 100: Rate = ₹5 per unit
# If units > 100: Rate = ₹7 per unit Display total bill amount.

units = int(input('Enter the units: '))

if units <= 100:
    total_bill = units * 5
else:
    total_bill = units * 7
print(f'Total bill amount: {total_bill}')