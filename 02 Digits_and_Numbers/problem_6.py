num_org = int(input("Enter A Two Digit Number : "))

num = num_org
last = num % 10
num = num //10
first = num % 10
rev = last * 10 + first
print("\n-:--------------------:-\n")
print("\tReverse of",num_org,"is :",rev)