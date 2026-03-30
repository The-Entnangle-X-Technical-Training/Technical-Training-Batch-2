#Problem 20: Electricity Bill (Simple)

unit = int(input("Enter number of unit : "))

rate = 5 if unit <= 100 else 7

el_bill = unit*rate

print(f"Your Bill : {el_bill}")