principal=int(input("Enter the principal amount: "))
rate=float(input("Enter the rate of interest: "))
time=int(input("Enter the time period: "))
SI=(principal*rate*time)/100
print("Simple interest: ",SI)
print("Total amount: ",principal+SI)