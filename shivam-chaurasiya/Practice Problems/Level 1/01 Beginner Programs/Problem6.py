# Percentage Calculator
# Write a program that takes marks in 3 subjects (out of 100 each) as input, calculates total marks out of 300 and percentage, then displays both.

math = float(input('Enter marks of math: '))
physics = float(input('Enter marks of physics: '))
chemistry = float(input('Enter marks of chemistry: '))

total_marks = math + physics + chemistry
percentage = (total_marks/300) * 100

print(f'Total Marks (out of 300): {total_marks}')
print(f'Percentage: {percentage:.2f}')