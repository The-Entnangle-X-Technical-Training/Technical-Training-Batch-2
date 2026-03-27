num = int(input("Enter A THREE DIGIT Number : "))
temp = num
last = temp % 10
temp = temp //10
mid = temp % 10
temp = temp //10
first = temp % 10
sod = last + mid + first
print("\n-:--------------------:-\n")
if num % sod == 0:
    print("\t",num,"is a HARSHAD NUMBER!")
else:
    print("\t",num,"is NOT a HARSHAD NUMBER!")