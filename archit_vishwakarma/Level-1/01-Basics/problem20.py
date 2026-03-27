sp= float(input('Enter Selling Price : '))
cp = float(input('Enter Cost Price : '))

difference = sp - cp

if difference > 0 :
    print(f'Profit of {difference}')
elif difference < 0:
    print(f'Loss of {abs(difference)}')
else:
    print('No loss no Profit its Breakeven')

