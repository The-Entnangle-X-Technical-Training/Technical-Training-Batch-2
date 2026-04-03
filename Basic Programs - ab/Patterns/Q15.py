#Horizontal Line of Stars
#Write a program that prints N stars in a horizontal line with spaces.
size=int(input("Enter the number of stars: "))
for i in range(size):
    print("*",end='  ')