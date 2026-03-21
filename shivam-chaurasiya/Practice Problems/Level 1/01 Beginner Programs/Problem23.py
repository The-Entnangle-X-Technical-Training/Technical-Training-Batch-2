# Electricity Bill Calculator
# Write a program that calculates electricity bill based on units consumed and rate per unit, then displays the total bill amount.


units_consumed = float(input('Enter the units consumed: '))
rate_per_unit = float(input('Enter rate per unit: '))

total_bill_amount = units_consumed*rate_per_unit
print(f'The total bill amount is: {total_bill_amount:.2f}')
