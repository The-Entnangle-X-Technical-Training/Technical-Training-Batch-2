#Write a program that takes three sides of a triangle as input and checks if it forms an 
#Equilateral (all sides equal), Isosceles (two sides equal), or Scalene (all sides different) triangle.
side1=int(input("Enter first side: "))
side2=int(input("Enter second side: "))
side3=int(input("Enter third side: "))
if(side1==side2==side3):
    print("Equilateral")
elif(side1==side2 or side1==side3 or side2==side3):
    print("Isosceles")
else:
    print("Scalene")