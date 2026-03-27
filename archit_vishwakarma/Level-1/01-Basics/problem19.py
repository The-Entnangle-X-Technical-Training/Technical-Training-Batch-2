p = float(input('Enter principal amount :'))
r = float(input('Enter Rate :'))
t = float(input('Enter Time :'))

si = (p*(r/100))*t

total_amt = p+si

print(f'Simple Intrest : {si}\nTotal amount : {total_amt}')