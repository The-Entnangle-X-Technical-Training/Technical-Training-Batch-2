num = int(input("Enter A Number : "))
sum = 0
temp = num
while temp != 0 :
    rim = temp % 10
    temp = temp // 10
    sum = sum + rim
print("\n-:-----SUM OF DIGITS OF {} IS {}-----:-\n".format(num,sum))