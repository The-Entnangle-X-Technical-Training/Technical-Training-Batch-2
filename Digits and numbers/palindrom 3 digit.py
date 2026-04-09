num=int(input("Enter a 3 digit number :"))
last_digit=num%10
middle_digit=(num//10)%10
first_digit=num%10
reverse=last_digit*100+middle_digit*10+first_digit
if(num==reverse):
    print("Palindrome")
else:
    print("Not Palindrome")
print(reverse)