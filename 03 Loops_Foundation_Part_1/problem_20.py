def fact(num):
    fct = 1
    for i in range(1,num+1):
        fct = fct * i
    return fct

num = int(input("Enter A Number : "))
facto = 0
temp = num
while temp != 0 :
    rim = temp % 10
    facto =  facto + int(fact(rim))
    temp = temp // 10
stg = "NOT A"
eq = "NOT EQUAL"
if num == facto :
    stg = "A"
    eq = "EQUAL"
print("\n-:-----SUM OF FACTORIAL OF DIGITS OF {} IS {},\n\tWHICH IS {} SO THIS {} STRONG NUMBER-----:-\n".format(num,facto,eq,stg))