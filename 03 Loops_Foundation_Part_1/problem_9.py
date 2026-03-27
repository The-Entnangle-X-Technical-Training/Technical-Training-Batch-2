num = int(input("Enter A Number : "))
count = num
sum = 0
start = 0 
while num != 0:
    if start % 2 != 0 :
        sum = sum + start
        num = num-1
    start = start + 1
print("\n-:-----SUM OF FIRST {} ODD NUMBERS IS {}-----:-\n".format(count,sum))