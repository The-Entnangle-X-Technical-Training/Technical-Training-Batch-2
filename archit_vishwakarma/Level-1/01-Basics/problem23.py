#Electricity Bill Calculator

unit = int(input("Enter unit consumed : "))
rate_per_unit = float(input("Enter rate/unit : "))

total_amt = rate_per_unit*unit

print(f"Total bill amount : {float(total_amt)}")