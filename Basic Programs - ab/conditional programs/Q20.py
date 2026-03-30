#Write a program that calculates electricity bill:
#  If units <= 100: Rate = ₹5 per unit
#  If units > 100: Rate = ₹7 per unit Display total bill amount.
unit=int(input("Enter the units: "))
if(unit<=100):
    print("Total Bill Amount: ", unit*5)
else:
    print("Total Bill Amount: ", unit*7)