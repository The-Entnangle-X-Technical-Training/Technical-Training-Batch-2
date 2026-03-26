#Problem 23: Check if Prime Number

number = int(input("Enter a number: "))
count = 0
for i in range(2, number):
    if number % i == 0:
        count = count + 1
if count == 0:
    print(number, "is prime")
else:
    print(number, "is not prime")