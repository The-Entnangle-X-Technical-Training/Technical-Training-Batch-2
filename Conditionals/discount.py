a=float(input("Enter Purchase Amount :"))
if(a>=100):
    discount=a*0.10
else:
    discount=0
final_amount=a-discount
print("Discount",discount)
print("Final Amount",final_amount)