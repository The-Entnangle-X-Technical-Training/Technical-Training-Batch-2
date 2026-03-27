num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
num3 = int(input("Enter Third Number : "))

if (num1 < num2) and (num1 < num3):
    print(num1,"is The SMALLEST NUMBER AMONG THREE")
elif (num2 < num1) and (num2 < num3):
    print(num2,"is The SMALLEST NUMBER AMONG THREE")
else:
    print(num3,"is The SMALLEST NUMBER AMONG THREE")