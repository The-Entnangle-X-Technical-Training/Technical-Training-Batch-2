#Write a program that takes marks (out of 100) as input and displays
#"Pass" if marks >= 40, otherwise displays "Fail".
marks=int(input("Enter your marks: "))
if(40 <= marks <=100):
    print("Pass")
else:
    print("Fail")