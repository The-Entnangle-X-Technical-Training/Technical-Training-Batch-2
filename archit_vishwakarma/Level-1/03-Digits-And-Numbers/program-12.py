n = input("\nEnter a number : ")

try:
    n = int(n)
    if n < 100 and n > 9:

        a = n//10
        b = n%10

        result = a-b

        z = (abs(result)+8)//9
        print(f"digit is : {'Not '*z + 'Palindrome' }\n")

    else:
        print("Enter a TWO Digit Number")
except ValueError:
    print("enter a valid number")