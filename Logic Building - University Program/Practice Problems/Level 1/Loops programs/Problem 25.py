#Problem 25: Power Calculator

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
final = 0

for i in range(1, exponent+1):
    final = base**i
print(base,"^",exponent,":", final)