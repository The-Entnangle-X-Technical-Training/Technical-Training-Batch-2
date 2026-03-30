#Write a program that gives discount based on purchase amount: 
# If amount >= 1000: 10% discount 
# Otherwise: No discount Display final amount after discount.
amount=int(input("Enter amount: "))
if(amount>=1000):
    print("Final Amount: ",amount-(amount*10)/100)
else:
    print("No Discount given and the Final Amount is: ", amount)