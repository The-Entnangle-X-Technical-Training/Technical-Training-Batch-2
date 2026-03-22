# Profit or Loss
# Write a program that takes cost price and selling price as input and displays whether there is "Profit", "Loss", or "No Profit No Loss".

cp = float(input('Enter the cost price: '))
sp = float(input('Enter the selling price: '))

if sp > cp:
    profit = sp - cp
    print("Profit")
elif sp < cp:
    loss = cp - sp
    print('Loss')
else:
    print('No Profit, No Loss')