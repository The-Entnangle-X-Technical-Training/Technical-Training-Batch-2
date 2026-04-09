num=int(input("Enter a 3 digit Number :"))
a1=num//100
a2=(num//10)%10
a3=num%10

if(a1<a2 and a2<a3):
    print("Digits are Ascending Order")
else:
    print("Digits are not Ascending Order")