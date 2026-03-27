sumd = 0
def sod(number):
    digi = 0
    global sumd
    if number != 0:
        digi = number%10
        sumd += digi
        return sod(number//10)
num_org = int(input("Enter A Number : "))
sod(num_org)
print("\n-:--------------------:-\n")
div = "NOT DIVISIBLE"
if sumd % 3 == 0:
    div = "DIVISIBLE"
print("\tSum of Digits of",num_org,"is",sumd,"\n\tAnd SOD is",div,"By 3")
