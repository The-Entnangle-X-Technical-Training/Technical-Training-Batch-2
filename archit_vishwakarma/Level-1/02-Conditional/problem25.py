amt = float(input("Enter Purchased amount : "))
if amt>=1000:
    discount = amt*10/100
    print(f"your bill with 10% discount is {amt - discount}")
else:
    print(f"your bill amount is {amt}")