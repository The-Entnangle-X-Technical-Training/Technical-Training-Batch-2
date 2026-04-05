N = input("Enter a number : ")

if N.isdigit():
    N = int(N)
    for i in range(1,N+1):
        print(i)
else:
    print("Enter a valid number")