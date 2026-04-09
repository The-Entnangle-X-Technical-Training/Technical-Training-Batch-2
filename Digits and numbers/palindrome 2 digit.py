num=int(input("Enter a 2 digit number :"))
last_digit=num%10
first_digit=num%10
reverse=last_digit*10+first_digit
if(num==reverse):
    print("Palindrome")
else:
    print("Not Palindrome")