#Write a program that takes three angles as input and checks if they can form a valid triangle (sum = 180). Display "Valid" or "Invalid".
angle1=int(input("Enter first angle: "))
angle2=int(input("Enter second angle: "))
angle3=int(input("Enter third angle: "))
if(angle1+angle2+angle3==180):
    print("Valid Triangle")
else:
    print("Invalid Triangle")