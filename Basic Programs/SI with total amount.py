P=int(input("Enter a Principle Amount :"))
R=int(input("Enter a Rate Of Interest :"))
T=int(input("Enter a Time Period :"))
SI=(P*R*T)/100
total_amount=P+SI
print("Simple Interest :",SI)
print("Total Amount :",total_amount)