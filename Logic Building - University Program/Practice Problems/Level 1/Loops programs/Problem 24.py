#Problem 24: Print All Numbers Divisible by 3 (1 to N)

number = int(input("Enter a number: "))
count = 0
for i in range(1, number+1):
    if i % 3 == 0:
        count = count +1
        print(i, end=" ")