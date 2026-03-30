#Write a program that takes marks (0-100) as input and displays grade: 
# A if marks >= 90 
# B if marks >= 70 
# C if marks >= 40 
# F if marks < 40
marks=int(input("Enter your marks: "))
if(90<=marks<=100):
    print("A")
elif(70<=marks<=89):
    print("B")
elif(40<=marks<=69):
    print("C")
elif(0<=marks<40):
    print("F")
else:
    print("Invalid")