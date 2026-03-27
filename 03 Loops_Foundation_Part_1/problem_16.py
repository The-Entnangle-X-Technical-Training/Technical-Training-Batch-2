num = int(input("Enter A Number : "))
pro = 1
temp = num
while temp != 0 :
    rim = temp % 10
    temp = temp // 10
    pro = pro * rim
print("\n-:-----PRODUCT OF DIGITS OF {} IS {}-----:-\n".format(num,pro))