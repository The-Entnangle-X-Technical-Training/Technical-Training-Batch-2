# Check if Number is Divisible by Both 2 and 3
# Write a program that checks if a number is divisible by both 2 and 3. Display "Yes" or "No".

num = int(input('Ener a number: '))

if num%2==0 and num%3==0:
    print('Yes')
else:
    print('No')