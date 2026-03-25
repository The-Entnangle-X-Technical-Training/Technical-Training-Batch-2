principal = int(input("Enter Principle Amount : "))
rate = int(input("Enter Rate : "))
years = int(input("Enter Time (IN YEARS ONLY) : "))

interest = (principal*rate*years)/100
total = principal+interest
print("\n--------INVOICE--------")
print("\tPrincipal :",principal,"RS")
print("\tRate :",rate,"%")
print("\tTime :",years,"years")
print("-------------------------")
print("\tInterest Amount :",interest)
print("\tTotal Amount with Interest:",total)