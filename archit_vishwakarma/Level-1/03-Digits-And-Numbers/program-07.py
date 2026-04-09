n = input("Enter a number : ")

try:
    n = int(n)
    if n < 1000 and n > 99:
        # a extracts for 100th digit
        # b extracts for 10th digit
        # c extracts for 1th digit

        a = n%10
        b = (n%100)//10
        c = n//100

        reverse = (a*100) + (b*10) + c
        print(f"Reverse of three number : {reverse}")

    else:
        print("Enter a Three Digit Number")
except ValueError:
    print("enter a valid number")