crnt_reading=int(input("Enter current reading: "))
prv_reading=int(input("Enter previous reading: "))
fixed_charge=92
tax=18
subsidies=500
rate_per_unit=8
total_unit=crnt_reading-prv_reading
energy_cost=total_unit*rate_per_unit
total_bill=energy_cost+fixed_charge+tax-subsidies
print("Total amount is: ",total_bill)