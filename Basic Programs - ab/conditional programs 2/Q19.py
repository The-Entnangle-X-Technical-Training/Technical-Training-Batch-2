#Write a program that takes x and y coordinates as input and displays which quadrant the point lies in (I,
#II, III, IV), or if it lies on an axis or origin.
x=int(input("Enter X-Coordinates: "))
y=int(input("Enter Y-Coordinates: "))
if(x==0 and y==0):
    print("X and Y are on Origin.")
elif(y==0 and x!=0):
    print("X Axis")
elif(x==0 and y!=0):
    print("Y Axis")
elif(x>0 and y>0):
    print("Quadrant 1")
elif(x<0 and y>0):
    print("Quadrant 2")
elif(x<0 and y<0):
    print("Quadrant 3")
elif(x>0 and y<0):
    print("Quadrant 4")