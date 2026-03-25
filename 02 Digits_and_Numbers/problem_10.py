num_org = int(input("Enter A Three Digit Number : "))

num = num_org
last = num % 10
num = num//10
mid = num % 10
num = num // 10
first = num % 10
product = last * mid * first
print("\n-:--------------------:-\n")
print("\tProduct of the digits of",num_org,"is :",product)