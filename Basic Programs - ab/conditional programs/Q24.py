#Write a program that takes temperature as input and displays: 
# "Cold" if temperature < 15
# "Normal" if temperature is 15-30
# "Hot" if temperature > 30
temp=int(input("Enter Temperature: "))
if(temp<15):
    print("Cold")
elif(15<=temp<=30):
    print("Normal")
else:
    print("Hot")