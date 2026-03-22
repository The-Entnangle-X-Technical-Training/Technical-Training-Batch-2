#Problem 21: Check Triangle Validity by Angles

first_angle = int(input("Enter the size of first angle: "))
second_angle = int(input("Enter the size of second angle: "))
third_angle = int(input("Enter the size of third angle: "))

if first_angle + second_angle + third_angle == 180:
    print("Valid triangle")
else:
    print("Invalid triangle")
