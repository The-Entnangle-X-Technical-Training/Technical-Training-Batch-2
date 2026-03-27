m = int(input("Enter A Multiple : "))
n = int(input("Enter The Range(LAST VALUE) : "))
count = 0
print("\n-:-----MULTIPLE OF {} FROM 1 TO {}-----:-\n".format(m,n))
for i in range(m,n+1):
    if i % m == 0:
        print("\t\t",i)
        count = count + 1
print("\nTotal",count,"Multiples of",m,"Found From 1 TO",n)