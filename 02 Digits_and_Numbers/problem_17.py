even =[]
def eve(num):
    global even
    if num != 0:
        rim = num % 10
        if rim % 2 == 0:
            even.append(rim)
        return eve(num // 10)
num = int(input("Enter A FOUR Digit Number : "))
eve(num)
print("\n-:--------------------:-\n")
print("\tThere are",len(even),"EVEN DIGITS in",num)
