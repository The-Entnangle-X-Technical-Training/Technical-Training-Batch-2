print('Enter principal ammount:',end="")
ammount=int(input())
print('Enter interest rate(per year):',end="")
rate=int(input())
print('Enter duration(time):',end="")
time=int(input())
simpleinterest=(ammount*rate*time)/100
totalammount=ammount+simpleinterest
print("Your principal ammount:",ammount)
print("Interest=",simpleinterest)
print("total ammont after interset:",totalammount)