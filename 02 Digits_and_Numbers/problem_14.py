num_org = int(input("Enter A Four Digit Number : "))

num = num_org
last = num % 10
num = num //10
third = num % 10
num = num // 10
second = num % 10
num = num // 10
first = num % 10
print("\n-:--------------------:-\n")
print(first,second,third,last)
if (first > second) and (first > third) and (first > last) :
    print("\t",first,"is THE LARGEST DIGIT in",num_org)
elif (second > first) and (second > third) and (second > last):
    print("\t",second,"is THE LARGEST DIGIT in",num_org)
elif (third > first) and (third > second) and (third > last):
    print("\t",third,"is THE LARGEST DIGIT in",num_org)
else:
    print("\t",last,"is THE LARGEST DIGIT in",num_org)