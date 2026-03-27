num = int(input("Enter A Number : "))
even = 0
odd = 0
temp = num
while temp != 0:
    rim = temp % 10
    if rim % 2 == 0 :
        even = even + 1
    else:
        odd = odd + 1
    temp = temp // 10
print("\n-:-----THERE ARE {} EVEN AND {} ODD NUMBERS IN {}-----:-\n".format(even,odd,num))