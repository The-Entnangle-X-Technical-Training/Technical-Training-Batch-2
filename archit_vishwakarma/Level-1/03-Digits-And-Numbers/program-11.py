n = input("\nEnter a number : ")

try:
    n = int(n)
    last_digit = n%10
    result = last_digit%2

    print(f"Last digit is : {'odd'*(result*1) +  'even'*((result-1)**2)}")

except ValueError:
    print("enter a valid number")