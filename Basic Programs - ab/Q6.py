sub1=int(input("Enter the marks of first subject(Out of 100):"))
if(sub1>100):
    print("Invalid marks entered for first subject. Please enter marks out of 100.")
    exit()
sub2=int(input("Enter the marks of second subject(Out of 100):"))
if(sub2>100):
    print("Invalid marks entered for second subject. Please enter marks out of 100.")
    exit()
sub3=int(input("Enter the marks of third subject(Out of 100):"))
if(sub3>100):
    print("Invalid marks entered for third subject. Please enter marks out of 100.")
    exit()
print("Total marks:",sub1+sub2+sub3)
print("Percentage:",(sub1+sub2+sub3)/3)