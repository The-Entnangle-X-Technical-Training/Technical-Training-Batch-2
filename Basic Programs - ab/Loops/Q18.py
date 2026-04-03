#Write a program that takes a number N and calculates its factorial (N! = 1×2×3×...×N).
num=int(input("Enter a number: "))
fact=1
for i in range(1,num+1):
    fact*=i
print(f'Factorial of number {num} is: ',fact)