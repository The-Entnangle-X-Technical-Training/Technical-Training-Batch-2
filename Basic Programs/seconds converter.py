a=int(input("Enter a Total Seconds :"))
hours=a//3600
seconds=a%3600
minutes=seconds//60
seconds=seconds%60
print("Hours :",hours)
print("Minutes :",minutes)
print("Seconds :",seconds)