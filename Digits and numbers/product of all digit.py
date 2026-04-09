num=int(input("Enter a 3 digit number :"))
first=num//100
middle=(num//10)%10
last=num%10
product=first*middle*last
print("Product of digits :",product)