a = int(input("enter angle 1 : "))
b = int(input("enter angle 2 : "))
c = int(input("enter angle 3 : "))

sum = a+b+c

result = "Valid" if sum == 180 and a>0 and b>0 and c>0  else "Invalid"

print(result)
