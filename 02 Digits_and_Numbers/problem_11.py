num = int(input("Enter a Number : "))
last = num % 10
print("\n-:--------------------:-\n")
if (last % 2 ==0 ):
    print("\tLast Digit",last,"in",num,"is An EVEN NUMBER")
else:
    print("\tLast Digit",last,"in",num,"is An ODD NUMBER")