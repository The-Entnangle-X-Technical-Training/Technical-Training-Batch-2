#Problem 17: Triangle Type by Sides

first_side = int(input("Enter side one: "))
second_side = int(input("Enter side two: "))
third_side = int(input("Enter side three: "))

if first_side == second_side and second_side == third_side and third_side == first_side:
    print("Equilateral Triangle")
elif first_side == second_side or second_side == third_side or third_side == first_side:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")