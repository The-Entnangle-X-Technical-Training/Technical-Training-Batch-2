num_org = int(input("Enter A Three Digit Number : "))
num = num_org
mid = num %10
num = num //10
mid = num % 10
print("\n-:--------------------:-\n")
print("Middle Digit of",num_org,"is ",mid)