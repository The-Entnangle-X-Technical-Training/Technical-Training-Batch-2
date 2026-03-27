num = int(input("Enter A Number : "))
rev = 0
temp = num
while temp != 0 :
    rim = temp % 10
    rev =  rev * 10 + rim
    temp = temp // 10
print("\n-:-----REVERSE OF DIGITS OF {} IS {}-----:-\n".format(num,rev))