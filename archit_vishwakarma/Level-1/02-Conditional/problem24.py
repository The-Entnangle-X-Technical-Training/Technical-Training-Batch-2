temp = float(input("enter temperature : "))
result = "Cold" if temp<15 else "Normal" if temp>15 and temp<30 else "Hot"
print(result)