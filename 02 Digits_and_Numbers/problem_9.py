num_org = int(input("Enter A Four Digit Number : "))

num = num_org
last = num % 10
num = num//100
num = num // 10
first = num % 10
avg = (last+first)/2
print("\n-:--------------------:-\n")
print("\tAverage of First :",first,"and Last :",last," Digits in",num_org,"is ",avg)