num=int(input("Enter a 4 digit number :"))
l1=num//1000
l2=(num//100)%10
l3=(num//10)%10
l4=num%10

print(l1)
print(l2)
print(l3)
print(l4)

largest=l1
if(l2>largest):
    largest=l2
if(l3>largest):
    largest=l3
if(l4>largest):
    largest=l4
print("Largest Number :",largest)