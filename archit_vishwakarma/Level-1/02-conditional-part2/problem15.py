num = input("Enter a number : ")

try:
    int_num = int(num)
    if len(num) == 1:
        print("Single Digit")
    elif len(num) == 2:
        print("Double Digit")
    else:
        print("More then double digit")
except ValueError:
    print("enter a valid number")