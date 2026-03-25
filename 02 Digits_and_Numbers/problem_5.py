num_org = int(input("Enter A Three Digit Number : "))
sum = 0
num = num_org
sum = sum + num % 10
num = num //10
sum = sum + num % 10
num = num //10
sum = sum + num % 10
num = num //10
print("\n-:--------------------:-\n")
print("Sum Of",num_org,"Digits is :",sum)