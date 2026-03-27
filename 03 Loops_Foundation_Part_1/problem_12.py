num = int(input("Enter A Number : "))
sum = 0
for i in range(num+1):
    sum = sum + i*i
print("\n-:-----SUM OF SQUARES FROM 1 TO {} IS {}-----:-\n".format(num,sum))