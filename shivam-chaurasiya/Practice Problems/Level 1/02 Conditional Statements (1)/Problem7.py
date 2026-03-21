# Pass or Fail
# Write a program that takes marks (out of 100) as input and displays "Pass" if marks >= 40, otherwise displays "Fail".

marks = float(input('Enter marks (out of 100): '))

if (marks >= 40 and marks<=100):
    print('Pass')
elif (marks >= 0 and marks < 40):
    print('Fail')
else:
    print('Please enter marks (out of 100)')