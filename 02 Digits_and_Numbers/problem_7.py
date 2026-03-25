num_org = int(input("Enter A Three Digit Number : "))

num = num_org
last = num % 10
num = num//10
mid = num % 10
num = num // 10
first = num % 10
rev = last * 100 + mid * 10 + first
print("\n-:--------------------:-\n")
print("\tReverse of",num_org,"is :",rev)