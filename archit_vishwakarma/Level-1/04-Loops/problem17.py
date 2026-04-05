N = input("Enter a number : ")

if N.isdigit():
    N = int(N)
    total = 0
    for i in range(1, N+1, +2):
        total += i
    print(total)
else:
    print("Enter a valid number")