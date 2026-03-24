# Grade Calculator (Simple)
# Write a program that takes marks (0-100) as input and displays grade:
# A if marks >= 90
# B if marks >= 70
# C if marks >= 40
# F if marks < 40

marks = float(input('Enter marks: '))

if marks >= 90:
    print('Grade: A')
elif marks >= 70:
    print('Grade: B')
elif marks >= 40:
    print('Grade: C')
else:
    print('Grade: F')