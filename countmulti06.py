num=int(input("Enter multiplication number:"))
n=int(input("Enter  number to multiple:"))
count=0
for i in range(1,num):
    if(i%n==0):
        count+=1
        print(i," ")
print("Count Number is:-",count)