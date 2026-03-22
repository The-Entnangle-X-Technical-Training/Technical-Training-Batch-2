# #Problem 16: Grade Calculator (Simple)

Marks = float(input("Enter marks: "))

if Marks >= 90:
    print("A Grade")
elif Marks >= 70:
    print("B Grade")
elif Marks >= 40:
    print("C Grade")
elif Marks < 40:
    print("F Grade")
else:
    print("Invalid")
