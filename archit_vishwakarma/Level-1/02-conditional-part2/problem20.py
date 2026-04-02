weight = input("Enter weight in kg : ")
height = input("Enter height in m : ")

try:
    w = float(weight)
    h = float(height)
    if w > 0 and h > 0:
        bmi = w/(h**2)
        if bmi < 18.5:
            print("Underweight")
        elif bmi < 25:
            print("Normal")
        elif bmi < 30:
            print("Overweight")
        else:
            print("Obese")
    else:
        print("Enter Positive value only")
except ValueError:
    print("Please enter valid value")