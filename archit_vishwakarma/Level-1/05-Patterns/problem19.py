# for even

n = int(input("Enter n : "))
for i in range(1, n):
    print(" "*(n-i) + "*"*i)

# for odd / perfect pyramis

n = int(input("Enter n : "))
for i in range(1, n):
    print(" "*(n-i) + "*"*(2*i-1))