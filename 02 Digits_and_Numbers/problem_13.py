num_org = int(input("Enter A Three Digit Number : "))

num = num_org
last = num % 10
num = num//10
mid = num % 10
num = num // 10
first = num % 10
print("\n-:--------------------:-\n")
if last == first :
    print("\tNumber",num_org,"is a PALINDROME NUMBER")
else:
    print("\tNumber",num_org,"is NOT A PALINDROME NUMBER")