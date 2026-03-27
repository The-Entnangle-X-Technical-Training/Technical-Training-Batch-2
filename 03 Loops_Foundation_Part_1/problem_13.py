num = int(input("Enter A Number : "))
count = 0
temp = num
while temp != 0 :
    temp = temp // 10
    count = count + 1
print("\n-:-----{} HAS {} DIGITS-----:-\n".format(num,count))