marks = input("Enter : ")

try:
    float_marks = float(marks)
    if float_marks<0 or float_marks>100:
        print("marks should be between 0 & 100")
    else:
        result = "Pass" if float_marks>= 40 else "fail"
        print(result)
except ValueError:
    print("Enter valid number")