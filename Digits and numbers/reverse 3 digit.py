num=int(input("Enter a 3 digit number :"))
reverse=(num%10)*100+((num//10)%10)*10+(num//100)
print("Reverse 2 digit :",reverse)