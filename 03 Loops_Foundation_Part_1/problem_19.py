num = int(input("Enter A Number : "))
rev = 0
temp = num
while temp != 0 :
    rim = temp % 10
    rev +=  rim * rim * rim
    temp = temp // 10
pal = "NOT AN"
if num == rev :
    pal = "AN"
print("\n-:-----SUM OF CUBES OF DIGITS OF NUMBER {} IS {} SO THIS IS {} ARMSTRONG NUMBER-----:-\n".format(num,rev,pal))