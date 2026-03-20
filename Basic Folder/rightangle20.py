print('Enter 1st Angles:',end="")
angle1=int(input())
print('Enter 2nd Angles:',end="")
angle2=int(input())
print('Enter 3rd Angles:',end="")
angle3=int(input())
if(angle1<90 and angle2<90 and angle3<90):
    print("This is Acute Angle")
elif(angle1==90 and angle2<90 and angle3<90):
     print("This is Right Angle Triangle:")
elif(angle1<90 and angle2==90 and angle3<90) :
     print("This is Right Angle Triangle:")
elif(angle1<90 and angle2<90 and angle3==90):
    print("This is Right Angle Triangle:")
elif(angle1>90 and angle2<90 and angle3<90):
     print("This is Obtus Angle Triangle:")
elif(angle1<90 and angle2>90 and angle3<90) :
     print("This is Obtus Angle Triangle:")
elif(angle1<90 and angle2<90 and angle3>90):
    print("This is  Obtus Angle Triangle:")
else:
   print("This is Not a Triangle:")  