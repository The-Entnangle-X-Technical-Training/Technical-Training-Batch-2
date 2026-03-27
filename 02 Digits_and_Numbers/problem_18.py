num = int(input("Enter A THREE DIGIT Number : "))
temp = num
last = temp % 10
temp = temp //10
mid = temp % 10
temp = temp //10
first = temp % 10
print("\n-:--------------------:-\n")
if (last > mid) and (mid > first):
    print("\tNumber",num,"is in ASCENDING ORDER")
else:
    print("\tNumber",num,"is NOT in ASCENDING ORDER")