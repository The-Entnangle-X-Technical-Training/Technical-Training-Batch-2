# Simple Interest with Total Amount

p = int(input('Enter the principal amout: '))
r = int(input('Enter the rate of interest: '))
t = int(input('Enter the time period: '))

simple_interest = (p*r*t)/100
total_amout = p+simple_interest

print('Simple Interest:', simple_interest)
print('Total Amount:', total_amout)