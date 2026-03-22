# Check Triangle Validity by Angles
# Write a program that takes three angles as input and checks if they can form a valid triangle (sum = 180). Display "Valid" or "Invalid".

a1 = int(input('Enter first angle: '))
a2 = int(input('Enter second angle: '))
a3 = int(input('Enter third angle: '))

sum = a1 + a2 + a3

if sum == 180:
    print('Valid')
else:
    print('Invalid')
    
    
    