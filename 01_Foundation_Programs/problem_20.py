angle1 = int(input("Enter First Angle Of Triangle : "))
angle2 = int(input("Enter Second Angle Of Triangle : "))
angle3 = int(input("Enter Third Angle Of Triangle : "))

if(angle1 + angle2 + angle3 == 180):
    print("\nThe Given Angles of Triangle will Form ",end='')
    if (angle1 < 90 and angle2 < 90 and angle3 < 90):
        print("An Acute Triangle")
    elif (angle1 == 90 or angle2 == 90 or angle3 == 90):
        print("An Right Triangle")
    elif (angle1 > 90 or angle2 > 90 or angle3 >90):
        print("An Obtuse Triangle")