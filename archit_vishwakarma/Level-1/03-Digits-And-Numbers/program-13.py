n = input("\nEnter a number : ")

try:
    n = int(n)
    if n < 1000 and n > 99:

        a = n//100
        b = n%10
        result = a-b

        z = (abs(result)+8)//9
        print(f"digit is : {'Not '*z + 'Palindrome' }\n")

    else:
        print("Enter a THREE Digit Number")
except ValueError:
    print("enter a valid number")