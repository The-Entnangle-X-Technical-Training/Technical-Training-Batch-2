#Write a program that takes base and exponent as input and calculates base^exponent using a loop.
base=int(input("Enter the base: "))
exponent=int(input("Enter the exponent: "))
result=1
for i in range(exponent):
    result = result*base
print("Result: ", result)