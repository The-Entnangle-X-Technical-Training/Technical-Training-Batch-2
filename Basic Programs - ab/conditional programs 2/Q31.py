#Write a program that takes coefficients a, b, c of quadratic equation ax²+bx+c=0, calculates discriminant (b²-4ac), and displays whether roots are real & distinct (D>0), real & equal (D=0), or imaginary (D<0).
a=float(input("Enter the value of 'a': "))
b=float(input("Enter the value of 'b': "))
c=float(input("Enter the value of 'c': "))
d=(b**2)-(4*a*c)
if(d>0):
    print("Real & Distinct (D>0)")
elif(d==0):
    print("Real & Equal (D=0)")
else:
    print("Imaginary (D<0)")