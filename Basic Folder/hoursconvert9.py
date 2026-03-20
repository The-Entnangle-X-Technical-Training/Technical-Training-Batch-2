print('Enter total Number of second:',end="")
a=int(input())
count=0
countt=0
while(a>=3600):
    a=a-3600
    count+=1
while(a>=60):
    a=a-60
    countt=countt+1
print(count,"Hour",end="")
print(" ",countt," Minutes",end="")
print(" ",a,"second")