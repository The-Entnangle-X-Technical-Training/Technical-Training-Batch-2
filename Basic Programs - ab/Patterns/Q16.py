#Problem 16: Vertical Line of Stars
#Write a program that prints N stars vertically (one per line).
size=int(input("Enter the number of stars: "))
for i in range(size):
    print("*", end='\n')