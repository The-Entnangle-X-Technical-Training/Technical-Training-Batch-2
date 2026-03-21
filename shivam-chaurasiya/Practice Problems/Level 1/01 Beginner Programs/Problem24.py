# BMI(Body Mass Index) Calculator
# Write a program that calculates Body Mass Index using: BMI = weight(kg) / (height(m))2


weight = float(input('Enter the weight(kg): '))
height = float(input('Enter the height(m): '))

bmi = weight / (height)**2
print(f'Body Mass Index is: {bmi:.2f}')

# Adding logic to display the category
if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi < 24.9:
    print("Category: Normal weight")
elif 25 <= bmi < 29.9:
    print("Category: Overweight")
else:
    print("Category: Obesity")