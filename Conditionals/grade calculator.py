a=float(input("Enter a Marks :"))
if(a<0 or a>100):
    print("Invalid marks")
elif(a>=90):
    print("Grade A")
elif(a>=70):
    print("Grade B")
elif(a>=40):
    print("Grade c")
else:
    print("Grade E")