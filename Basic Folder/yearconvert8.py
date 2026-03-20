print('Enter total Number of days:',end="")
a=int(input())
count=0
countt=0
while(a>=365):
    a=a-365
    count+=1
while(a>=30):
    a=a-30
    countt=countt+1
print(count,"Year",end="")
print(" ",countt," Month",end="")
print(" ",a,"Days")