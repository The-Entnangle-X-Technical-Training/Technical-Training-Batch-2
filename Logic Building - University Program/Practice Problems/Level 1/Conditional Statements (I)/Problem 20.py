#Problem 20: Electricity Bill (Simple)

units = float(input("enter the units consumed: "))

if units <= 100:
    print("The subtotal bill amount is ", units*5, "rupees (5 rupees per unit)") 
elif units > 100:
    print("The subtotal bill amount is ", units*7, "rupees (7 rupees per unit)")
else:
    print("invalid")