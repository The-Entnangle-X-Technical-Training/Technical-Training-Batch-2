num = int(input("Enter A Number : "))
print("\n-:-----FIRST {} EVEN NUMBERS-----:-\n".format(num))
start = 0
while num != 0:
    if start % 2 == 0 :
        print("\t\t",start)
        num = num-1
    start = start + 1
