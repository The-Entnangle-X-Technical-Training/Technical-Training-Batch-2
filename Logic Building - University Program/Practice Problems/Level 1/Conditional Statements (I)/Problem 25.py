#Problem 25: Simple Discount Calculator

amount = int(input("Enter the purchase amount: "))

if amount >= 1000:
    print("The final amount is", amount - (amount * (10/100)), "rupees (10% discount!)")
else:
    print("The final amount is", amount, "rupees (No discount)")