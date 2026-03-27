num = int(input("Enter A Number : "))
po = int(input("Enter Power Count : "))
res = 1
for  i in range(po):
    res = res * num
print("\n-:-----POWER OF {} ^ {} IS {}-----:-\n".format(num,po,res))
