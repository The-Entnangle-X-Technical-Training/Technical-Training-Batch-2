a = int(input("Enter a :"))
b = int(input("Enter b :")) 
c = int(input("Enter c :"))

if a==b==c :
    print("All number are equal")
else:
    check = "a" if a<b and a<c else "b" if b<c else "c"
    print(check)