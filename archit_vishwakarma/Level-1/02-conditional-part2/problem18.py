# a, b, c are three sides of triangle

a = input("Enter side 1 : ")
b = input("Enter Side 2 : ")
c = input("Enter Side 3 : ")

try:
    a = float(a)
    b = float(b)
    c = float(c)

    if a>0 and b>0 and c>0:
        if a+b>c and a+c>b and b+c>a:
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Enter Positive numbers")
except ValueError:
    print("Enter valid numbers")