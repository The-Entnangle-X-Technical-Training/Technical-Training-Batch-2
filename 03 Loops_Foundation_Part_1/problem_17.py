num = int(input("Enter A Number : "))
rev = 0
temp = num
while temp != 0 :
    rim = temp % 10
    rev =  rev * 10 + rim
    temp = temp // 10
pal = "NOT A"
if num == rev :
    pal = "A"
print("\n-:-----REVERSE OF NUMBER {} IS {} SO THIS IS {} PALINDROME NUMBER-----:-\n".format(num,rev,pal))