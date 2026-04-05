N = input("Enter a number : ")

if N.isdigit():
    N = int(N)
    for i in range(0,N+1,+2):
        print(i)
else:
    print("Enter a valid number")
