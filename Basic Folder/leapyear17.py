print('Enter Year to chek(Leap Year):',end="")
num=int(input())
if(num%100==0):
    if num%400==0:
        print("This is Leap Year:")
    else:
        print("This is Not Leap Year:")
elif num%4==0:
    print("This is Leap Year:")
else:
    print("This is Not Leap Year:")