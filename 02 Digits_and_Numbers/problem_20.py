num = int(input("Enter A FOUR Digit Number : "))
temp = num // 1000
first = temp % 10
print("\n-:--------------------:-\n")
if (first != 0) :
    print("\t",num,"is A DUCK NUMBER!")
else:
    print("\t",num,"is NOT A DUCK NUMBER!")