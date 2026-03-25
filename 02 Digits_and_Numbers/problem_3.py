num_org = int(input("Enter A Three Digit Number : "))
num = num_org
first = num % 10
num =num//10
first = num % 10
num = num // 10
first = num % 10
print("\n-:--------------------:-\n")
print("First Digit of",num_org,"is ",first)