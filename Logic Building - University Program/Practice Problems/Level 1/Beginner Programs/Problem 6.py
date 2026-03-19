#Problem 6: Percentage Calculator

First_Subject = float(input("Enter the marks of first subject: "))
Second_Subject = float(input("Enter the marks of second subject: "))
Third_Subject = float(input("Enter the marks of third subject: "))

Total = First_Subject + Second_Subject + Third_Subject
Percentage = (Total/300) * 100

print("Total marks: ", Total, "/ 300")
print("Percentage: ", Percentage, "%")