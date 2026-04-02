age = input("Enter your age : ")

try:
    int_age = int(age)
    if int_age <=0 or int_age >150:
        print("Please enter valid age")
    else:
        result = "Eligible" if int_age>=18 else "Not Eligible"
        print(result)
except ValueError:
    print("Please enter Valid Age")